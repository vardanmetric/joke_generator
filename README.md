# Random Joke or Quote Generator

A simple Python command-line application that fetches and displays a random joke or quote from public APIs. Perfect for beginners to practice working with APIs and user input in Python!

## Features

* Get a random joke (setup and punchline)
* Get a random quote (with author)
* Simple command-line interface
* Graceful error handling

## Requirements

* Python 3.7+
* `requests``(https://pypi.org/project/requests/)

## Installation

1. **Clone or download the repository**

21. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

31. **Run the script**

   ```bash
   python random_joke_quote_generator.py
   ```

## Usage

When you run the script, you’ll see:

```
Welcome to the Random Joke or Quote Generator!

Type 'joke' for a joke, 'quote' for a quote, or 'exit' to quit:
```

* Enter `joke` to get a random joke.
* Enter `quote` to get a random quote.
* Enter `exit` to quit the program.

Example:

```
Type 'joke' for a joke, 'quote' for a quote, or 'exit' to quit: joke

Joke:
Why don't scientists trust atoms?
Because they make up everything.
```

## APIs Used


 [Official Joke API](https://official-joke-api.appspot.com/)
* [Quotable API](https://api.quotable.io/)

## Customization

Feel free to extend the project by:
* Adding more APIs (e.g., for facts, riddles, or advice)
* Building a GUI version with Tkinter

 Saving favourite jokes/quotes to a file
