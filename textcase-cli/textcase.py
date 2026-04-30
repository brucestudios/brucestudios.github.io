#!/usr/bin/env python3
"""
textcase - A command-line tool to convert text to different cases.

Usage:
    textcase [OPTIONS] [TEXT]

Options:
    -u, --upper          Convert to uppercase
    -l, --lower          Convert to lowercase
    -t, --title          Convert to title case
    -s, --sentence       Convert to sentence case
    -a, --alternating    Convert to alternating case (e.g., hElLo)
    -r, --reverse        Reverse the string
    -c, --capitalize     Capitalize each word (like title but without forcing lower on the rest)
    -h, --help           Show this help message

If TEXT is not provided, reads from standard input.

Examples:
    echo "hello world" | textcase --upper
    textcase --title "hello world"
    textcase --sentence "HELLO WORLD. this is a test."
"""

import argparse
import sys
import re


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def to_title(text):
    return text.title()


def to_sentence(text):
    """Convert to sentence case: first letter of each sentence capitalized."""
    if not text:
        return text
    
    # Split by sentence endings (.!?) followed by space or end of string
    sentences = re.split(r'([.!?]+(?:\s|$))', text)
    result = []
    
    for i in range(0, len(sentences), 2):
        sentence = sentences[i]
        if sentence:
            # Capitalize first letter, rest as is
            sentence = sentence[0].upper() + sentence[1:] if sentence else sentence
        result.append(sentence)
        if i + 1 < len(sentences):
            result.append(sentences[i + 1])  # Add the delimiter
    
    return ''.join(result)


def to_alternating(text):
    """Convert to alternating case: hElLo WoRlD"""
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    return ''.join(result)


def to_reverse(text):
    return text[::-1]


def to_capitalize(text):
    """Capitalize each word: Hello World"""
    return ' '.join(word.capitalize() for word in text.split())


def main():
    parser = argparse.ArgumentParser(
        description="Convert text to different cases",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  echo "hello world" | textcase --upper
  textcase --title "hello world"
  textcase --sentence "HELLO WORLD. this is a test."
        """
    )
    
    parser.add_argument('text', nargs='*', help='Text to convert (if not provided, reads from stdin)')
    parser.add_argument('-u', '--upper', action='store_true', help='Convert to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', help='Convert to lowercase')
    parser.add_argument('-t', '--title', action='store_true', help='Convert to title case')
    parser.add_argument('-s', '--sentence', action='store_true', help='Convert to sentence case')
    parser.add_argument('-a', '--alternating', action='store_true', help='Convert to alternating case')
    parser.add_argument('-r', '--reverse', action='store_true', help='Reverse the string')
    parser.add_argument('-c', '--capitalize', action='store_true', help='Capitalize each word')
    
    args = parser.parse_args()
    
    # Get input text
    if args.text:
        input_text = ' '.join(args.text)
    else:
        input_text = sys.stdin.read().rstrip('\n')
    
    # If no transformation specified, just output the text
    if not any([args.upper, args.lower, args.title, args.sentence, 
                args.alternating, args.reverse, args.capitalize]):
        print(input_text)
        return
    
    # Apply transformations in order
    result = input_text
    
    if args.upper:
        result = to_upper(result)
    if args.lower:
        result = to_lower(result)
    if args.title:
        result = to_title(result)
    if args.sentence:
        result = to_sentence(result)
    if args.alternating:
        result = to_alternating(result)
    if args.reverse:
        result = to_reverse(result)
    if args.capitalize:
        result = to_capitalize(result)
    
    print(result)


if __name__ == '__main__':
    main()