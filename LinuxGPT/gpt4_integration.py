import requests
from config import OPENAI_API_KEY

class GPT4Integration:
    def __init__(self):
        self.api_key = OPENAI_API_KEY

    def get_response(self, query):
        url = "https://api.openai.com/v1/engines/davinci-codex/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "prompt": query,
            "max_tokens": 50,
            "n": 1,
            "stop": None,
            "temperature": 1
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            json_data = response.json()
            return json_data['choices'][0]['text'].strip()
        else:
            print("Error in OpenAI API:", response.status_code)
            return None
