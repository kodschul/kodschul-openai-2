
from openai import OpenAI
from chatbot.env import API_KEY


client = OpenAI(api_key=API_KEY)


prompt = '''
sadsada

asdashdahsdsa

sadsahdsahjd

This is a sample
{
    "slug": "the-journey-of-web-development",
    "title": "The Journey of Web Development",
    "image_url": "https://images.unsplash.com/photo-1720048169970-9c651cf17ccd?q=80&w=2028&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "author": "Jane Doe",
    "publish_date": "2023-09-12",
    "content": "-"
  },
'''


initial_prompt = "Du bist ein Rohm Semiconductor GmbH-Assistent, du wirst Kundenservice agieren und unsere repräsentieren, falls du etwas nicht weiß, bitte leitet den Kunden auf unsere Webseite weiter: rohm.com"

messages = [{"role": "system", "content": initial_prompt},
            {"role": "system", "content": "The CEO of our company is Markus Vitz"},]


def get_chat_response(prompt):

    messages.append({"role": "user",
                     "content":  prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",

        messages=messages,  # type:ignore
        stream=False,
    )

    response_message = response.choices[0].message.content

    return response_message
