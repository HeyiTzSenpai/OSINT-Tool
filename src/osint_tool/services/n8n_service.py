import requests
from osint_tool import config

class N8NService:
    def __init__(self):
        self.api_key = config.N8N_API_KEY
        self.webhook_url = config.N8N_WEBHOOK_URL

    def search(self, query: str) -> str:
        """
        Sends a query to the n8n AI Agent and returns the output.
        """
        payload = {"query": query}
        headers = {"X-N8N-API-KEY": self.api_key}

        response = requests.post(self.webhook_url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        output_md = data.get("output", "")

        if not output_md:
            raise ValueError("No 'output' field found in response")

        return output_md
