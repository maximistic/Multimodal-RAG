import requests
import time

# API URLs and headers for both models
SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
CHATBOT_API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

SENTIMENT_HEADERS = {"Authorization": "Bearer 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"}
CHATBOT_HEADERS = {"Authorization": "Bearer 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"}

def query_api(api_url, headers, payload, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                print(f"Chatbot: I'm having trouble with the API. Let's try again later.")
                return None

def get_sentiment_label(sentiment_response):
    if sentiment_response and isinstance(sentiment_response, list) and len(sentiment_response) > 0:
        # Assuming the response structure based on Hugging Face's common output format
        sentiment = sentiment_response[0]
        if 'label' in sentiment:
            return sentiment['label']
    return None

def chatbot():
    print("Chatbot: Hello! I'm a chatbot powered by BlenderBot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! I hope you have a great day. Take care.")
            break
        # Sentiment Analysis
        sentiment_response = query_api(SENTIMENT_API_URL, SENTIMENT_HEADERS, {"inputs": user_input})
        sentiment_label = get_sentiment_label(sentiment_response)
        
        # Generate chatbot response
        chatbot_response = query_api(
            CHATBOT_API_URL,
            CHATBOT_HEADERS,
            {"inputs": user_input, "parameters": {"max_length": 100, "temperature": 0.7}}
        )
        print(sentiment_label)
        if chatbot_response and isinstance(chatbot_response, dict) and 'generated_text' in chatbot_response:
            chatbot_text = chatbot_response['generated_text'].strip()
            if sentiment_label:
                print(f"Chatbot (Sentiment: {sentiment_label}): {chatbot_text}")
            else:
                print("Chatbot:", chatbot_text)
        else:
            print("Chatbot: I'm having trouble understanding. Could you rephrase that?")

if __name__ == "__main__":
    chatbot()
