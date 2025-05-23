from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")





system_prompt = """
You are an AI Assistant who is specialized in maths.
You should not answer any query that is not related to maths.

For a given query help user to solve that along with explanation.

Exmaple:
Input: 2 + 2
Output: 2 + 2 is 4 which is calcualted by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by multiplying 3 by 10. Fun fact, you can even multiply 10 * 3 which gives same result.

Input: Why is sky blue?
Output: Bruh? You alright? Is it maths query?
"""


client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

result = client.chat.completions.create(
    model='gemini-2.0-flash',
    messages=[
        # System prompt
          {'role': 'system', 'content': system_prompt},
          {'role': 'user', 'content': 'why pink is pink'}  
    ]
)

print(result.choices[0].message.content)