import random
import sys

QUOTES = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It always seems impossible until it's done. – Nelson Mandela",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "The best way to predict the future is to create it. – Peter Drucker",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
]

def main():
    quote = random.choice(QUOTES)
    print(quote)
    return 0

if __name__ == "__main__":
    sys.exit(main())