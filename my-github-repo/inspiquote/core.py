import json
import os
import random

def load_quotes():
    """Load quotes from the JSON file."""
    # Path to the quotes.json file, relative to this module
    module_dir = os.path.dirname(__file__)
    quotes_path = os.path.join(module_dir, 'quotes.json')
    with open(quotes_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['quotes']

def get_random_quote():
    """Return a random quote as a string."""
    quotes = load_quotes()
    quote = random.choice(quotes)
    return f'"{quote["text"]}" – {quote["author"]}'