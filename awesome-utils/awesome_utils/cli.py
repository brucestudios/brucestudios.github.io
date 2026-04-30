"""Command-line interface for awesome-utils."""

import argparse
from . import strings, files

def main():
    parser = argparse.ArgumentParser(description="Awesome Utils CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # strings subcommand
    strings_parser = subparsers.add_parser("strings", help="String utilities")
    strings_sub = strings_parser.add_subparsers(dest="subcommand", help="String subcommands")

    capitalize_parser = strings_sub.add_parser("capitalize", help="Capitalize words")
    capitalize_parser.add_argument("--text", required=True, help="Text to capitalize")

    reverse_parser = strings_sub.add_parser("reverse", help="Reverse string")
    reverse_parser.add_argument("--text", required=True, help="Text to reverse")

    palindrome_parser = strings_sub.add_parser("palindrome", help="Check palindrome")
    palindrome_parser.add_argument("--text", required=True, help="Text to check")

    # files subcommand
    files_parser = subparsers.add_parser("files", help="File utilities")
    files_sub = files_parser.add_subparsers(dest="subcommand", help="File subcommands")

    ensure_dir_parser = files_sub.add_parser("ensure-dir", help="Ensure directory exists")
    ensure_dir_parser.add_argument("--path", required=True, help="Directory path")

    args = parser.parse_args()

    if args.command == "strings":
        if args.subcommand == "capitalize":
            result = strings.capitalize_words(args.text)
            print(result)
        elif args.subcommand == "reverse":
            result = strings.reverse_string(args.text)
            print(result)
        elif args.subcommand == "palindrome":
            result = strings.is_palindrome(args.text)
            print(result)
    elif args.command == "files":
        if args.subcommand == "ensure-dir":
            path = files.ensure_dir(args.path)
            print(f"Ensured directory: {path}")

if __name__ == "__main__":
    main()