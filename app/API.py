# Examples


import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()  # or use dotenv_path if needed

API_KEY = os.getenv("QUIZ_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Make sure QUIZ_API_KEY is in your .env file.")

url = "https://quizapi.io/api/v1/questions"
params = {
    "apiKey": API_KEY,
    "limit": 10
}

response = requests.get(url, params=params)
print("Status:", response.status_code)
print(response.json())