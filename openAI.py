import openai
# from secret import OPEN_AI
import os

openai.api_key = os.environ.get('OPEN_AI')


def message_return(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0]["message"]["content"].strip()