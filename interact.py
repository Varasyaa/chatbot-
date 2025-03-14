def chat_with_bot(user_input):
    response = conversation.predict(input=user_input)
    return response
