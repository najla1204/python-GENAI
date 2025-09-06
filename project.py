import streamlit as st
from google import genai

bot = genai.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")
st.title("My GenAI App")
business_name = st.text_input("What is your business name: ")
business_descrip = st.text_input("Describe your business briefly..")
traget_audi = st.text_input("who is your target audience")
current_Capital = st.text_input("Enter the current captital")
location = st.text_input("Which location....")
if st.button("Click"):
    if business_name and business_descrip and traget_audi and current_Capital and location:
        question = (
        f"My business name is called {business_name}"
        f"It is described as : {business_descrip}"
        f"My target audience is: {traget_audi}"
        f"Our current capital is {current_Capital}"
        f"We are  starting in {location}"
    )
        question += "Can you provide suggestions to improve and grow my business?"
        response = bot.models.generate_content(model="gemini-1.5-flash",contents=[question])

        st.write(response.text)
    else:
        st.error("Please fill in all required fields.")
