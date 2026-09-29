import os
from pathlib import Path
from dotenv import load_dotenv

current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent

load_dotenv(parent_dir / ".env")
load_dotenv(current_dir / ".env", override=True)

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
model = os.getenv("DEEPSEEK_MODEL_ID")

if not api_key:
    raise RuntimeError("未读取到 DEEPSEEK_API_KEY，请检查 ch4/.env 或 ch4/autogen/.env")

print(f"API Key: {api_key[:10]}...")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
