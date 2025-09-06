from google import genai as na
bot = na.Client(api_key="AIzaSyAfoYIESxs_OxZK0v21JyWEa7KIsky4V4s")
mymem = bot.chats.create(model="gemini-1.5-flash")


while True:
    user = input("user: ")
    if user.lower()=="q":
        print("exit")
        break
    response = mymem.send_message(user)


    print("GenAI",response.text)
for mesg in mymem.get_history(user):
    print(f'{mesg.role.capitalize()}:{mesg.parts[0].text}')
