import os
import google.generativeai as genai
import json
import re

class AIService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-flash-latest')

    async def analyze_code(self, code: str, analysis_type: str) -> dict:
        prompt = self._construct_prompt(code, analysis_type)
        
        try:
            response = self.model.generate_content(prompt)
            return self._parse_response(response.text)
        except Exception as e:
            print(f"AI Analysis failed: {e}")

            return {
                "issues": [{"type": "error", "line": 0, "message": f"AI Error: {str(e)}"}],
                "optimized_code": code,
                "explanation": "Failed to analyze code due to an error."
            }

    def _construct_prompt(self, code: str, analysis_type: str) -> str:
        return f"""
        You are an expert Senior Software Engineer performing a code review.
        Task: {analysis_type} (Review, Bug Fix, or Optimization)

        Analyze the following code snippet:
        ```
        {code}
        ```

        Return the response in strictly valid JSON format with the following structure:
        {{
            "issues": [
                {{"line": <line_number>, "type": "bug|style|warning", "message": "<description>"}}
            ],
            "optimized_code": "<full_rewritten_code>",
            "explanation": "<brief_summary_of_changes>"
        }}

        Do not include markdown checks (```json). Just the raw JSON.
        """

    def _parse_response(self, text: str) -> dict:
        # cleanup markdown code blocks if present
        text = re.sub(r'```json\s*|\s*```', '', text)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "issues": [{"type": "error", "line": 0, "message": "Failed to parse AI response"}],
                "optimized_code": "// Error parsing AI response",
                "explanation": "The AI response was not valid JSON: " + text[:100]
            }
