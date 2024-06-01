import openai

# Set up OpenAI API
openai.api_key = 'sk-proj-iv8cVVB9x8IXYn0ZeO76T3BlbkFJNGBWf7PDxRwm5DbPUtW2'

# Function to get response from OpenAI API
def get_openai_response(user_input):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Sorry, I couldn't process your request due to an error: {e}"

# Simple Rule-Based Chatbot with Consultation Functionality
def chatbot_response(user_input):
    # Convert the user input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()
    
    # Define responses for specific inputs
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I'm ChatGPT, your friendly chatbot assistant."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "consult" in user_input or "ask" in user_input:
        return consult_assistant()
    else:
        return get_openai_response(user_input)

# Function to simulate consultation with the assistant
def consult_assistant():
    return "[Assistant] How can I assist you today?"

# Main loop to interact with the chatbot
def main():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
