import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Prompt-Guard-86M"
headers = {"Authorization": "Bearerhf_azQjmwiCwLjFzIvSiKSwPuSiNxXXROYacW"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        response = query({
            "inputs": user_input,
        })
        
        # The exact structure of the response may vary depending on the model
        # You might need to adjust this part based on the actual response format
        if isinstance(response, list) and len(response) > 0:
            print("Chatbot:", response[0]['generated_text'])
        else:
            print("Chatbot: I'm sorry, I couldn't generate a response.")

if __name__ == "__main__":
    chatbot()