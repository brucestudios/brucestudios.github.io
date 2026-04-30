"""Command-line interface for textutils."""

import argparse
import sys
from . import core
from . import utils


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Text utilities for password generation, passphrase creation, and text processing."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Password subcommand
    password_parser = subparsers.add_parser(
        "password", help="Generate a secure password"
    )
    password_parser.add_argument(
        "-l", "--length", type=int, default=16, help="Length of the password (default: 16)"
    )
    password_parser.add_argument(
        "-n", "--no-special", action="store_true", help="Exclude special characters"
    )
    password_parser.add_argument(
        "-d", "--no-digits", action="store_true", help="Exclude digits"
    )
    password_parser.add_argument(
        "-c", "--lower-only", action="store_true", help="Generate lowercase letters only"
    )
    password_parser.add_argument(
        "-u", "--upper-only", action="store_true", help="Generate uppercase letters only"
    )

    # Passphrase subcommand
    passphrase_parser = subparsers.add_parser(
        "passphrase", help="Generate a passphrase"
    )
    passphrase_parser.add_argument(
        "-w", "--words", type=int, default=4, help="Number of words (default: 4)"
    )
    passphrase_parser.add_argument(
        "-s", "--separator", type=str, default="-", help="Separator between words (default: '-')"
    )

    # Analyze subcommand
    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze text (word, line, character count)"
    )
    analyze_parser.add_argument(
        "text", nargs="?", type=str, help="Text to analyze. If not provided, reads from stdin."
    )
    analyze_parser.add_argument(
        "-f", "--file", type=str, help="Read text from a file instead of stdin or argument."
    )

    # Transform subcommand
    transform_parser = subparsers.add_parser(
        "transform", help="Transform text (upper, lower, title)"
    )
    transform_parser.add_argument(
        "text", nargs="?", type=str, help="Text to transform. If not provided, reads from stdin."
    )
    transform_parser.add_argument(
        "-f", "--file", type=str, help="Read text from a file instead of stdin or argument."
    )
    transform_parser.add_argument(
        "-t", "--type", choices=["upper", "lower", "title"], required=True, help="Transformation type"
    )

    # Palindrome subcommand
    palindrome_parser = subparsers.add_parser(
        "palindrome", help="Check if text is a palindrome"
    )
    palindrome_parser.add_argument(
        "text", nargs="?", type=str, help="Text to check. If not provided, reads from stdin."
    )
    palindrome_parser.add_argument(
        "-f", "--file", type=str, help="Read text from a file instead of stdin or argument."
    )

    # Random string subcommand
    random_parser = subparsers.add_parser(
        "random", help="Generate a random string"
    )
    random_parser.add_argument(
        "-l", "--length", type=int, default=16, help="Length of the string (default: 16)"
    )
    random_parser.add_argument(
        "-n", "--no-special", action="store_true", help="Exclude special characters"
    )
    random_parser.add_argument(
        "-d", "--no-digits", action="store_true", help="Exclude digits"
    )
    random_parser.add_argument(
        "-c", "--lower-only", action="store_true", help="Generate lowercase letters only"
    )
    random_parser.add_argument(
        "-u", "--upper-only", action="store_true", help="Generate uppercase letters only"
    )

    args = parser.parse_args()

    if args.command == "password":
        # Handle mutually exclusive options for password
        if args.lower_only and args.upper_only:
            parser.error("Options --lower-only and --upper-only are mutually exclusive")

        if args.lower_only:
            use_lower = True
            use_upper = False
            use_digits = False
            use_special = False
        elif args.upper_only:
            use_lower = False
            use_upper = True
            use_digits = False
            use_special = False
        else:
            use_lower = True
            use_upper = True
            use_digits = not args.no_digits
            use_special = not args.no_special

        try:
            password = core.generate_password(
                length=args.length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_digits=use_digits,
                use_special=use_special,
            )
            print(password)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "passphrase":
        try:
            passphrase = core.generate_passphrase(
                num_words=args.words,
                separator=args.separator,
            )
            print(passphrase)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "analyze":
        # Determine input source
        if args.file:
            try:
                with open(args.file, 'r', encoding='utf-8') as f:
                    text = f.read()
            except OSError as e:
                print(f"Error reading file: {e}", file=sys.stderr)
                sys.exit(1)
        elif args.text is not None:
            text = args.text
        else:
            text = sys.stdin.read()

        print(f"Words: {utils.count_words(text)}")
        print(f"Lines: {utils.count_lines(text)}")
        print(f"Characters: {utils.count_chars(text)}")

    elif args.command == "transform":
        # Determine input source
        if args.file:
            try:
                with open(args.file, 'r', encoding='utf-8') as f:
                    text = f.read()
            except OSError as e:
                print(f"Error reading file: {e}", file=sys.stderr)
                sys.exit(1)
        elif args.text is not None:
            text = args.text
        else:
            text = sys.stdin.read()

        if args.type == "upper":
            result = utils.to_upper(text)
        elif args.type == "lower":
            result = utils.to_lower(text)
        else:  # title
            result = utils.to_title(text)
        print(result, end='')

    elif args.command == "palindrome":
        # Determine input source
        if args.file:
            try:
                with open(args.file, 'r', encoding='utf-8') as f:
                    text = f.read()
            except OSError as e:
                print(f"Error reading file: {e}", file=sys.stderr)
                sys.exit(1)
        elif args.text is not None:
            text = args.text
        else:
            text = sys.stdin.read()

        if utils.is_palindrome(text):
            print("Yes")
        else:
            print("No")

    elif args.command == "random":
        # Handle mutually exclusive options for random string
        if args.lower_only and args.upper_only:
            parser.error("Options --lower-only and --upper-only are mutually exclusive")

        if args.lower_only:
            use_lower = True
            use_upper = False
            use_digits = False
            use_special = False
        elif args.upper_only:
            use_lower = False
            use_upper = True
            use_digits = False
            use_special = False
        else:
            use_lower = True
            use_upper = True
            use_digits = not args.no_digits
            use_special = not args.no_special

        try:
            random_str = utils.random_string(
                length=args.length,
                use_upper=use_upper,
                use_lower=use_lower,
                use_digits=use_digits,
                use_special=use_special,
            )
            print(random_str)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()