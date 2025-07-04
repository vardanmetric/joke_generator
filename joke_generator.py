import requests
import random

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        joke = response.json()
        return f"\nJoke:\n{joke['setup']}\n{joke['punchline']}"
    except Exception as e:
        return f"Error fetching joke: {e}"

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        quote = response.json()
        return f"\nQuote:\n\"{quote['content']}\"\n— {quote['author']}"
    except Exception as e:
        return f"Error fetching quote: {e}"

def main():
    print("Welcome to the Random Joke or Quote Generator!\n")
    while True:
        choice = input("Type 'joke' for a joke, 'quote' for a quote, or 'exit' to quit: ").strip().lower()
        if choice == 'joke':
            print(get_random_joke())
        elif choice == 'quote':
            print(get_random_quote())
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print("Please enter 'joke', 'quote', or 'exit'.")

if __name__ == "__main__":
    main()