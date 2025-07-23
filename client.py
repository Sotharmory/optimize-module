from google import genai
from google.genai import types
from config import API_KEY, MODEL_NAME

def get_client():
    return genai.Client(api_key=API_KEY)

def generate_response(client, prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(),
    )
    return response.text
