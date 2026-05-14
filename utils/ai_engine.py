import os
import requests

# =========== Load API key from environment variable ===========
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not found! Please set it in your .env file.")

# =========== Groq Chat API endpoint & model ===========
# Replace with your actual Groq API endpoint
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b-versatile"

# =========== AI call function ===========
def ask_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful academic assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_completion_tokens": 800,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except requests.exceptions.HTTPError as http_err:
        return f"❌ API HTTP Error {response.status_code}: {response.text}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"❌ Connection Error: {str(conn_err)}"
    except Exception as e:
        return f"❌ Request Failed: {str(e)}"