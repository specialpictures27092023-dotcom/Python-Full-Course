import time

# Simple response dictionary
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How are you today?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure! You can ask me anything.",
}

def get_bot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Sorry, I didn't understand that."

def main():
    print("🤖 Auto Reply ChatBot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Chat ended. Bye!")
            break
        response = get_bot_response(user_input)
        time.sleep(1)  # Simulate thinking
        print("Bot:", response)

if __name__ == "__main__":
    main()