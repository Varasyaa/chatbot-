from langchain.memory import ConversationBufferMemory

# Initialize memory
memory = ConversationBufferMemory()

# Set up the conversation chain with memory
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)
