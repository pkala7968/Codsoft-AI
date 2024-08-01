# function to get a response based on input
def chatbot_response(user_input):
    # Convert to lowercase to ensure no case sensitive errors
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you! How can I assist you?"
    
    elif "your name" in user_input:
        return "I'm a simple chatbot created by a developer. What's your name?"
    
    elif "weather" in user_input:
        return "I can't provide real-time weather updates, but it's always a good idea to check a weather website or app!"
    
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Run the chatbot in a loop till user wants to exit
def run_chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

run_chatbot()