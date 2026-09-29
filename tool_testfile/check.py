import os
from dotenv import load_dotenv

load_dotenv()

keys = [
    "OPENAI_API_KEY",
    "OPENAI_BASE_URL",
    "OPENAI_MODEL_ID",
    "TAVILY_API_KEY",
]

for key in keys:
    value = os.environ.get(key)
    if value:
        print(f"{key}: 已配置，前几位是 {value[:6]}...")
    else:
        print(f"{key}: 未配置")