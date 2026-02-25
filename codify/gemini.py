import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

def review_code(language, code):
    # Configure Gemini with API key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # Load Gemini Flash Lite model
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    # Prompt for AI
    prompt = f"""
You are an expert {language} code reviewer.

Tasks:
1. First, rate the code correctness in percentage.
2. Do line-by-line error detection.
3. Explain each mistake clearly.
4. Suggest improvements.
5. Provide the corrected final code.

User Code:
{code}
"""


    # Generate response
    response = model.generate_content(prompt)

    # Return AI result
    return response.text

    print(settings.GEMINI_API_KEY)