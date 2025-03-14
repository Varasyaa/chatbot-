if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"Chatbot: {response}")
