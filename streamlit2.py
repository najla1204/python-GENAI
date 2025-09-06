import streamlit as str
from google import genai as na

mybot = na.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")
mymem = mybot.chats.create(model="gemini-1.5-flash")
str.title("welcome...")
str.title("how can i help you code....")
user = str.text_input("enter any coding related questions....")
if str.button("click"):
    user += (f"you are a coding assistant that only answers coding related questions using the provided coding"
             "if a question is asked which is not related to coding content, reply with:"
             "'please enter quetions related to coding...'")
    response = mymem.send_message(user)
    str.write(response.text)
