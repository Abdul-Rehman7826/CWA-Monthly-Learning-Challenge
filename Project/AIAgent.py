import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

# Initialize Groq client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",   
)

def ask_groq(prompt: str, system: str = "You are a helpful assistant.") -> str:
    """Send a prompt to Groq and return the response."""
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",          
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

def main():
    print("⚡ Welcome to the Groq AI Assistant! (Using free tier)")
    while True:
        print("\nChoose an option:")
        print("1. Generate a story")
        print("2. Translate text")
        print("3. Answer a question")
        print("4. Exit")
        choice = input("> ").strip()

        if choice == "1":
            topic = input("What should the story be about? ")
            prompt = f"Write a short, imaginative story about: {topic}. Keep it under 200 words."
            print("\n📖 Generating story...\n")
            print(ask_groq(prompt))

        elif choice == "2":
            text = input("Enter the text to translate: ")
            lang = input("Translate to which language? ")
            prompt = f"Translate the following to {lang}. Only return the translation, no extra text.\n\n{text}"
            system_msg = "You are a translator. Provide only the translation."
            print("\n🌍 Translating...\n")
            print(ask_groq(prompt, system=system_msg))

        elif choice == "3":
            question = input("Ask anything: ")
            print("\n🤔 Thinking...\n")
            print(ask_groq(question))

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()