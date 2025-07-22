"""
design a simple rule-based chatbot using if-else conditions(min 5 respoonses)
"""

def chatbot():
    print("Hello! I'm Chatbot")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you today?")
        elif "your name" in user_input:
            print("Bot: I'm ChatSimple, your rule-based chatbot!")
        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif "weather" in user_input:
            print("Bot: I'm not connected to the internet, but I hope it's sunny where you are!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

chatbot()