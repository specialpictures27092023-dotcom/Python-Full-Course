import os
from openai import OpenAI

# 🔐 Use environment variable for security
api_key = os.getenv("OPENAI_API_KEY", "your-backup-key-here")

client = OpenAI(api_key=api_key)

response = client.Chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."
        },
        {
            "role": "user",
            "content": "what is coding"
        }
    ]
)

print(response.choices[0].message.content)