#!/usr/bin/env python3
"""
Inspirational Quotes Generator
Prints a random inspirational quote.
"""

import random

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. – Aristotle",
    "Whoever is happy will make others happy too. – Anne Frank",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt",
    "In the end, it's not the years in your life that count. It's the life in your years. – Abraham Lincoln",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
]

def main():
    print(random.choice(quotes))

if __name__ == "__main__":
    main()
