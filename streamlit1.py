import streamlit as str
from google import genai as na

mybot = na.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")

str.title("welcome to najla's page")
file = str.file_uploader("upload a file....")

response = mybot.models.generate_content(model="gemini-1.5-flash",
                                            contents=[file,"tell about this file"])
str.write(response.text)

