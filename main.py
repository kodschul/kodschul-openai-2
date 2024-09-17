
from openai import OpenAI
from env import API_KEY


client = OpenAI(api_key=API_KEY)


initial_prompt = "Du bist ein Rohm Semiconductor GmbH-Assistent, du wirst Kundenservice agieren und unsere repräsentieren, falls du etwas nicht weiß, bitte leitet den Kunden auf unsere Webseite weiter: rohm.com"


def get_chat_response(prompt):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": initial_prompt},
            {"role": "system", "content": "The CEO of our company is Markus Vitz"},
            {"role": "user",
             "content":  prompt}],
        stream=True,
    )

    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            response += chunk.choices[0].delta.content

    return response


print("Willkommen bei Rohm KI-Kundenservice!")
print("---------------")

while True:

    user_input = input("\nDu: ")

    if user_input.lower() == "q":
        print("Schönen Tag noch!")
        break

    print("\nKundenservice: ")
    get_chat_response(user_input)


# response = client.chat.completions.create(

#     model="",
#     messages=[{
#         "role": "user",
#         "content": "",
#     }]
#     max_tokens=500)
