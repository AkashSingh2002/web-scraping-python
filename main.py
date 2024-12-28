from openai import OpenAI
import requests
from bs4 import BeautifulSoup

base_url = "https://api.aimlapi.com/v1"
api_key = "api_key"
system_prompt = "You are a web-scraper chatbot. Be descriptive and helpful."

api = OpenAI(api_key=api_key, base_url=base_url)

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        title = soup.title.string if soup.title else "No title found"
        
        paragraphs = soup.find_all('p')
        paragraph_texts = [para.get_text() for para in paragraphs[:5]]  
        extracted_info = "\n".join(paragraph_texts)
        
        return f"Title: {title}\n\nExtracted Information:\n{extracted_info}"
    except Exception as e:
        return f"Error scraping the website: {str(e)}"

def main():
    conversation = [{"role": "system", "content": system_prompt}]
    
    print("Welcome! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if "http" in user_input:
            scraped_data = scrape_website(user_input)
            conversation.append({"role": "system", "content": f"The scraped data from the website is: {scraped_data}"})
        
        conversation.append({"role": "user", "content": user_input})
        
        completion = api.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=conversation,
            temperature=0.7,
            max_tokens=256,
        )
        
        response = completion.choices[0].message.content
        
        print("AI:", response)
        
        conversation.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
