from langchain import OpenAI, ConversationChain

# Initialize the OpenAI module with your API key
llm = OpenAI(api_key='your-openai-api-key')

# Set up the conversation chain
conversation = ConversationChain(llm=llm, verbose=True)
