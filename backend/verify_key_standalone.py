import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(f"Loaded Key: '{api_key}'")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

try:
    print("Attempting to generate content...")
    response = model.generate_content("Hello, world!")
    print("Success:", response.text)
except Exception as e:
    print("Error:", e)
