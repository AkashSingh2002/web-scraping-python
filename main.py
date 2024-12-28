from openai import OpenAI

base_url = "https://api.aimlapi.com/v1"
api_key = "59959821edbd4fafa1937305e9ddfc54"
system_prompt = "You are a web-scrapper chatbot. Be descriptive and helpful."

api = OpenAI(api_key=api_key, base_url=base_url)

def main():
    # Start the conversation with the system prompt
    conversation = [{"role": "system", "content": system_prompt}]
    
    print("Welcome! Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if user says 'exit'
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Add user's input to the conversation history
        conversation.append({"role": "user", "content": user_input})
        
        # Generate response from the AI
        completion = api.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=conversation,
            temperature=0.7,
            max_tokens=20,
        )
        
        # Get the AI's response
        response = completion.choices[0].message.content
        
        # Print the conversation
        print("AI:", response)
        
        # Add AI's response to the conversation history
        conversation.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
