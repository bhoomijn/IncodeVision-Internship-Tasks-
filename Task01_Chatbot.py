# Task 01 - Simple Chatbot
# Internship: IncodeVision
# Author: Devendra (bhoomijn)
# Description: A simple rule-based chatbot that responds to basic user inputs.

def chatbot():
    print("🤖 Welcome to the Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("Bot: I'm a simple chatbot created for the IncodeVision internship tasks.")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that. Try asking something else.")

if __name__ == "__main__":
    chatbot()
