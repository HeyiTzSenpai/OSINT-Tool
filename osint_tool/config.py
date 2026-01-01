import os

from dotenv import load_dotenv

load_dotenv()

N8N_API_KEY = os.getenv("N8N_API_KEY")

if not N8N_API_KEY:
    raise Exception("N8N_API_KEY not found")
