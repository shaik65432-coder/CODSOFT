from datetime import datetime

print("===================================")
print("      SIMPLE RULE-BASED CHATBOT")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")


def chatbot_response(user_input):

    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I am fine and always ready to chat with you."

    elif "your name" in user_input:
        return "I am a simple AI chatbot created using Python."

    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence."

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Current time is {current_time}"

    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}"

    elif "thank" in user_input:
        return "You're welcome!"
    
    elif "favorite color" in user_input:
        return "I like blue because it represents technology."

    elif "developer" in user_input:
        return "My developer is a Computer Science student."

    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that yet."


while True:

    user_message = input("You: ")

    response = chatbot_response(user_message)

    print("Bot:", response)

    if "bye" in user_message.lower():
        break