import argparse
import random
import string
import sys


def generate_password(length=16, use_numbers=False, use_symbols=False,
                      use_lower=False, use_upper=False):
    """Generate a password with given options."""
    # If no flags are specified, use all categories
    if not any([use_numbers, use_symbols, use_lower, use_upper]):
        use_numbers = use_symbols = use_lower = use_upper = True

    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(random.choice(characters) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(
        description="Generate a secure random password."
    )
    parser.add_argument(
        "-l", "--length", type=int, default=16,
        help="Length of password (default: 16)"
    )
    parser.add_argument(
        "-n", "--numbers", action="store_true",
        help="Include numbers (0-9)"
    )
    parser.add_argument(
        "-s", "--symbols", action="store_true",
        help="Include symbols (!@#$%^&* etc.)"
    )
    parser.add_argument(
        "-lw", "--lower", action="store_true",
        help="Include lowercase letters (a-z)"
    )
    parser.add_argument(
        "-up", "--upper", action="store_true",
        help="Include uppercase letters (A-Z)"
    )

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_numbers=args.numbers,
            use_symbols=args.symbols,
            use_lower=args.lower,
            use_upper=args.upper
        )
        print(password)
    except ValueError as e:
        parser.error(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()