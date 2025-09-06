import streamlit as str
from google import genai as gen

bot = gen.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")
str.title("business support model..")
name = str.text_input("enter your business name:")
desc = str.text_input("describe your business precisely here : ")
target = str.text_input("who are your target audience : ")
cap = str.text_input("what is your capital investment : ")
loc = str.text_input("in which location are you trying to start your business : ")
if str.button(" get suggestion "):
    if name and desc and target and cap and loc :
        prompt = (
            f"my business name is {name}"
            f"description of my business is {desc}"
            f"my target audience are {target}"
            f"my capital investment is {cap}"
            f"the location i want to start my business is {loc}"
        )
        prompt += "give me business ideas and suggestions for me based on the given data to improvise my idea and get my business better reached"
        response = bot.models.generate_content(model="gemini-1.5-flash",contents=[prompt])
        str.write(response.text)
    else:
        str.write("please provide valid informations....")
