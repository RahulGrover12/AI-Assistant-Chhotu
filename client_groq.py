import os

from groq import Groq

client = Groq(
    api_key="YOUR_API_KEY",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is coding?",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)