import os
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel

# Load API key from .env file
load_dotenv("API.env")  # Ensure the correct filename is passed

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Error: API key not found. Please check your .env file.")

# Configure the Gemini API
configure(api_key=api_key)

def get_gemini_response(model, question):
    try:
        result = model.generate_content(question)
        return result.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("Suggestions to reduce accident severity")
    model_name = "models/gemini-pro"
    model = GenerativeModel(model_name)

    while True:
        user_question = input("You: ")
        if user_question.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Stay safe!")
            break

        response = get_gemini_response(model, user_question)

        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: Sorry, I couldn't fetch a response. Please try again later.")

if __name__ == "__main__":
    main()
