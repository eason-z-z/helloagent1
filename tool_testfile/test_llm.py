import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_BASE_URL")
model_id = os.environ.get("OPENAI_MODEL_ID")

print("API_KEY 是否读取到：", bool(api_key))
print("BASE_URL:", base_url)
print("MODEL_ID:", model_id)

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

response = client.chat.completions.create(
    model=model_id,
    messages=[
        {"role": "user", "content": "你好，请用一句话介绍你自己。"}
    ],
)

print(response.choices[0].message.content)