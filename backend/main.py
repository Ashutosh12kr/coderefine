from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os
from ai_service import AIService

# Load env variables
load_dotenv()

app = FastAPI(title="CodeRefine API", description="AI-Powered Code Review & Optimization Engine")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI Service
ai_service = None
try:
    ai_service = AIService()
except Exception as e:
    print(f"Warning: AI Service not initialized. Missing API Key? {e}")

class CodeRequest(BaseModel):
    code: str
    analysis_type: str

class CodeAnalysis(BaseModel):
    issues: list[dict]
    optimized_code: str
    explanation: str

@app.get("/")
def read_root():
    return {"message": "Welcome to CodeRefine API"}

@app.post("/analyze", response_model=CodeAnalysis)
async def analyze_code(request: CodeRequest):
    if not ai_service:
        raise HTTPException(status_code=500, detail="AI Service not configured (missing API Key)")
    
    result = await ai_service.analyze_code(request.code, request.analysis_type)
    return CodeAnalysis(**result)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
