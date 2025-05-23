from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

result = client.chat.completions.create(
    model='gemini-2.0-flash',
    messages=[
        # System prompt
        {'role': 'system', 'content': 'You are an ai assistant whose name is myOwnTech'},
        {'role': 'user', 'content': 'Hey there, what is your name? I am Bhupesh'}
    ]
)

print(result.choices[0].message.content)