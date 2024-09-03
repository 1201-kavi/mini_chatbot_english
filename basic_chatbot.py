from transformers import pipeline, Conversation

# Load the pre-trained model for conversational tasks
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def chat_with_bot():
    print("Chatbot: Hello! I'm your friendly chatbot. Ask me anything!")
    
    # Create a conversation object to maintain context
    conversation = Conversation()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Append user input to the conversation
        conversation.add_user_input(user_input)
        
        # Generate a response
        response = chatbot(conversation)
        
        # Print the chatbot's response
        print("Chatbot:", response.generated_responses[-1])

# Run the chatbot
chat_with_bot()
