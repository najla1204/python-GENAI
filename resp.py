from PIL import Image
from google import genai as na
bot = na.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")
img = Image.open("pytimg.jpg  ")
response = bot.models.generate_content(model="gemini-1.5-flash",
                                       contents=[img,"tell me more about the image"])
print(response.text)
