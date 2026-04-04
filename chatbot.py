import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I help you today?"

    # Asking name
    elif "What is your name" in user_input:
        return "I am a chatbot."

    # Asking about user
    elif "how are you" in user_input:
        return "I'm doing great!"

    # Help
    elif "help" in user_input:
        return "I can answer simple questions. Try asking about time, date, or greetings!"

    # Time
    elif "time" in user_input:
        from datetime import datetime
        return "Current time is: " + datetime.now().strftime("%H:%M:%S")

    # Date
    elif "date" in user_input:
        from datetime import datetime
        return "Today's date is: " + datetime.now().strftime("%Y-%m-%d")

    # Exit
    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a nice day!"

    # Default response
    else:
        return "Sorry, I didn't understand that. Can you try something else?"

def run_chatbot():
    print("Chatbot: Hi Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if response == "Goodbye! Have a nice day!":
            break

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()