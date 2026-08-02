import ollama
from google import genai

from config import (
    LLM_PROVIDER,
    OLLAMA_MODEL,
    GEMINI_API_KEY
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_response(prompt):

    if LLM_PROVIDER == "gemini":

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]