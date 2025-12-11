from groq import Groq
from .config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def agent_reply(message):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional AI agent able to do tasks using provided tools."},
            {"role": "user", "content": message},
        ],
        stream=False
    )
    return response.choices[0].message.content

