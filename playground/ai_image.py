
from openai import OpenAI
from env import API_KEY


client = OpenAI(api_key=API_KEY)


prompt = "An image describing AI & IT"

response = client.images.generate(
    model="dall-e-3", prompt=prompt, size="1024x1024")


image_url = response.data[0].url

print(image_url)
