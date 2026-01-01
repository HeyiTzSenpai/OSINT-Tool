import os

from dotenv import load_dotenv

load_dotenv()

N8N_API_KEY = os.getenv("N8N_API_KEY")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

if not N8N_API_KEY:
    raise Exception("N8N_API_KEY not found")
if not N8N_WEBHOOK_URL:
    raise Exception("N8N_WEBHOOK_URL not found")
