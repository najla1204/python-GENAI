from google import genai as GA
import streamlit as st
from PIL import Image

bot = GA.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")

UserData = st.file_uploader("choose file")
img = Image.open(UserData)
user_input = st.text_input("User ")
if st.button("Predict"):
    user_input += (f"You are a helpful assistant that only answers questions using the provided file data. "
                 "If a question is not related to the file content, reply with: " 
                 "'Please ask a question based on the contents of your uploaded file.'")
    response = bot.models.generate_content(model="gemini-1.5-flash",
                                           contents=[img, user_input])
    st.write(response.text)
