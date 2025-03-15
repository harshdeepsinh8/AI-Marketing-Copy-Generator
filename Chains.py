import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AIChain:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama3-8b-8192"

    
    def generate_marketing_copy(self, brand, description, audience, tone):
        """Generates marketing copy using Groq Cloud API."""
        prompt = f"""
        Generate a marketing ad copy for the following details:
        Brand: {brand}
        Product/Service: {description}
        Target Audience: {audience}
        Tone: {tone}

        Provide:
        - A catchy headline
        - A short marketing description (2-3 sentences)
        - Three relevant hashtags
        - A call-to-action (CTA)
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert marketing copywriter."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        response_data = response.json()

        if "choices" in response_data:
            return response_data["choices"][0]["message"]["content"].strip()
        else:
            return "Error: Unexpected API response. Please check the API key or model settings."
