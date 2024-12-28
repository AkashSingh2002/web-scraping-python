from openai import OpenAI
import requests
from bs4 import BeautifulSoup

base_url = "https://api.aimlapi.com/v1"
api_key = "59959821edbd4fafa1937305e9ddfc54"
system_prompt = "You are a web-scraper chatbot. Be descriptive and helpful."

api = OpenAI(api_key=api_key, base_url=base_url)

# Web scraping function using BeautifulSoup
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract the title of the page
        title = soup.title.string if soup.title else "No title found"
        
        # Extract some paragraphs from the page to provide context
        paragraphs = soup.find_all('p')
        paragraph_texts = [para.get_text() for para in paragraphs[:5]]  # Get first 5 paragraphs
        extracted_info = "\n".join(paragraph_texts)
        
        return f"Title: {title}\n\nExtracted Information:\n{extracted_info}"
    except Exception as e:
        return f"Error scraping the website: {str(e)}"

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
        
        # If user input includes a URL, scrape the website
        if "http" in user_input:
            scraped_data = scrape_website(user_input)
            conversation.append({"role": "system", "content": f"The scraped data from the website is: {scraped_data}"})
        
        # Add user's input to the conversation history
        conversation.append({"role": "user", "content": user_input})
        
        # Generate response from the AI
        completion = api.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=conversation,
            temperature=0.7,
            max_tokens=256,
        )
        
        # Get the AI's response
        response = completion.choices[0].message.content
        
        # Print the conversation
        print("AI:", response)
        
        # Add AI's response to the conversation history
        conversation.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
