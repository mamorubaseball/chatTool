import openai
from secret import OPEN_AI

openai.api_key =  OPEN_AI

def message_return(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "大谷翔平について教えて"},
        ],
    )
    return response.choices[0]["message"]["content"].strip()