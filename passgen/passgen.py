#!/usr/bin/env python3
"""
passgen - A simple secure password generator.

Generate strong random passwords of desired length.
"""

import argparse
import string
import secrets
import sys


def generate_password(length: int = 16) -> str:
    """Generate a random password of given length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Ensure at least one of each character type
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument(
        "-l", "--length", type=int, default=16,
        help="Length of the password (default: 16)"
    )
    parser.add_argument(
        "-n", "--number", type=int, default=1,
        help="Number of passwords to generate (default: 1)"
    )
    args = parser.parse_args()

    if args.length < 4:
        print("Error: Password length must be at least 4 to include all character types.", file=sys.stderr)
        sys.exit(1)

    for _ in range(args.number):
        print(generate_password(args.length))


if __name__ == "__main__":
    main()