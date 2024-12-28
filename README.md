# Web Scraper Chatbot

This project is a chatbot that can interact with users and scrape content from websites based on user-provided URLs. It uses the `BeautifulSoup` library to extract relevant data (e.g., the page title and a few paragraphs) from the provided URL. The chatbot then generates responses based on the scraped data and responds to users' questions, continuously interacting with them until they type 'exit'.

## Features

- **Web Scraping**: Scrapes the title and content from a website using BeautifulSoup and Requests.
- **Dynamic Conversation**: Responds to user queries by integrating scraped data into the chatbot's responses.
- **Endless Interaction**: Allows continuous interaction with the user until they type 'exit'.
- **AI Integration**: Uses the AIML API to generate AI-powered responses.

## Requirements

This project requires Python 3.x and the following libraries:
- `openai` - for interacting with the AIML API.
- `requests` - for sending HTTP requests to scrape websites.
- `beautifulsoup4` - for parsing HTML and extracting data from websites.

## Setup and Installation

### Step 1: Install Python and Dependencies
Make sure you have Python 3.x installed. You can then install the required libraries by using the `requirements.txt` file.

### Step 2: Install Required Libraries

1. Clone the repository or download the project files.
2. Navigate to the project directory and install the required libraries:

```bash
pip install -r requirements.txt
