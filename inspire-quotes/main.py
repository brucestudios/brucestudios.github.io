#!/usr/bin/env python3
"""
Inspire Quotes - A simple Python application that generates inspirational quotes
"""

import random
import sys
from typing import List

class QuoteGenerator:
    def __init__(self):
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "Whoever is happy will make others happy too. - Anne Frank",
            "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
            "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
            "Life is what happens when you're busy making other plans. - John Lennon",
            "Spread love everywhere you go. Let no one ever come to you without leaving happier. - Mother Teresa",
            "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt",
            "Always remember that you are absolutely unique. Just like everyone else. - Margaret Mead",
            "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson",
            "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
            "Change your thoughts and you change your world. - Norman Vincent Peale",
            "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "It always seems impossible until it's done. - Nelson Mandela",
            "What we achieve inwardly will change outer reality. - Plutarch",
            "You miss 100% of the shots you don't take. - Wayne Gretzky",
            "The best revenge is massive success. - Frank Sinatra",
            "You must be the change you wish to see in the world. - Mahatma Gandhi",
            "When we are no longer able to change a situation, we are challenged to change ourselves. - Viktor Frankl",
            "Act as if what you do makes a difference. It does. - William James",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
            "Turn your wounds into wisdom. - Oprah Winfrey",
            "The more you praise and celebrate your life, the more there is in life to celebrate. - Oprah Winfrey",
            "Be the reason someone believes in the goodness of people. - Unknown",
            "One day or day one. You decide. - Unknown",
            "The only disability in life is a bad attitude. - Scott Hamilton",
            "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
            "Do something today that your future self will thank you for. - Unknown",
            "Difficulties in life are intended to make us better, not bitter. - Dan Reeves",
            "Don't let yesterday take up too much of today. - Will Rogers",
            "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
            "Why fit in when you were born to stand out? - Dr. Seuss",
            "Fall seven times, stand up eight. - Japanese Proverb",
            "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. - Henry Ford",
            "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
            "Your limitation—it's only your imagination. - Unknown",
            "Push yourself, because no one else is going to do it for you. - Unknown",
            "Sometimes later becomes never. Do it now. - Unknown",
            "Great things never come from comfort zones. - Unknown",
            "Dream it. Wish it. Do it. - Unknown",
            "Success doesn't just find you. You have to go out and get it. - Unknown",
            "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
            "Don't stop when you're tired. Stop when you're done. - Unknown",
            "Wake up with determination. Go to bed with satisfaction. - Unknown",
            "Do something today that your future self will thank you for. - Unknown",
            "What seems to us as bitter trials are often blessings in disguise. - Oscar Wilde",
            "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde",
            "Be yourself; everyone else is already taken. - Oscar Wilde",
            "Always forgive your enemies; nothing annoys them so much. - Oscar Wilde",
            "We are all in the gutter, but some of us are looking at the stars. - Oscar Wilde",
            "Experience is merely the name men gave to their mistakes. - Oscar Wilde",
            "To love oneself is the beginning of a lifelong romance. - Oscar Wilde",
            "Never love anyone who treats you like you're ordinary. - Oscar Wilde",
            "Life is too short to be lived for others. - Unknown",
            "Do not wait for leaders; do it alone, person to person. - Mother Teresa",
            "Kind words can be short and easy to speak, but their echoes are truly endless. - Mother Teresa",
            "If you can't feed a hundred people, then feed just one. - Mother Teresa",
            "Love begins at home, and it is not how much we do... but how much love we put in that action. - Mother Teresa",
            "Peace begins with a smile. - Mother Teresa",
            "Let us always meet each other with smile, for the smile is the beginning of love. - Mother Teresa",
            "The most terrible poverty is loneliness, and the feeling of being unloved. - Mother Teresa",
            "If we have no peace, it is because we have forgotten that we belong to each other. - Mother Teresa",
            "Spread love everywhere you go. Let no one ever come to you without leaving happier. - Mother Teresa",
            "I alone cannot change the world, but I can cast a stone across the waters to create many ripples. - Mother Teresa",
            "The good you do today will be forgotten tomorrow. Do good anyway. - Mother Teresa",
            "Honesty and transparency make you vulnerable. Be honest and transparent anyway. - Mother Teresa",
            "What you spend years building may be destroyed overnight. Build anyway. - Mother Teresa",
            "People really need help but may attack you if you do help them. Help people anyway. - Mother Teresa",
            "Give the world the best you have and you'll get kicked in the teeth. Give the world the best you have anyway. - Mother Teresa"
        ]

    def get_random_quote(self) -> str:
        """Return a random inspirational quote."""
        return random.choice(self.quotes)

    def get_quote_by_index(self, index: int) -> str:
        """Return a quote by its index."""
        if 0 <= index < len(self.quotes):
            return self.quotes[index]
        raise IndexError("Quote index out of range")

    def list_quotes(self) -> List[str]:
        """Return all quotes."""
        return self.quotes.copy()

def main():
    """Main entry point for the application."""
    generator = QuoteGenerator()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--list":
            for i, quote in enumerate(generator.list_quotes(), 1):
                print(f"{i}. {quote}")
            return
        elif sys.argv[1] == "--help":
            print("Inspire Quotes - Generate inspirational quotes")
            print("Usage:")
            print("  inspire-quotes          # Get a random quote")
            print("  inspire-quotes --list   # List all quotes")
            print("  inspire-quotes --help   # Show this help")
            return
        else:
            try:
                index = int(sys.argv[1]) - 1
                print(generator.get_quote_by_index(index))
            except ValueError:
                print("Error: Argument must be a number or --list/--help")
                sys.exit(1)
            except IndexError:
                print(f"Error: Quote index must be between 1 and {len(generator.quotes)}")
                sys.exit(1)
    else:
        print(generator.get_random_quote())

if __name__ == "__main__":
    main()