import argparse
from .core import get_random_quote

def main():
    parser = argparse.ArgumentParser(
        description="Generate a random inspirational quote."
    )
    parser.add_argument(
        '-v', '--version', action='version', version='%(prog)s 1.0.0'
    )
    args = parser.parse_args()
    quote = get_random_quote()
    print(quote)

if __name__ == '__main__':
    main()