"""Text processing utilities."""

def count_words(text: str) -> int:
    """Count the number of words in the text.

    Args:
        text: The input text.

    Returns:
        The number of words.
    """
    # Split by whitespace and filter out empty strings
    words = text.split()
    return len(words)


def count_lines(text: str) -> int:
    """Count the number of lines in the text.

    Args:
        text: The input text.

    Returns:
        The number of lines.
    """
    # Split by line boundaries
    lines = text.splitlines()
    return len(lines)


def count_chars(text: str) -> int:
    """Count the number of characters in the text.

    Args:
        text: The input text.

    Returns:
        The number of characters.
    """
    return len(text)


def to_upper(text: str) -> str:
    """Convert text to uppercase.

    Args:
        text: The input text.

    Returns:
        The text in uppercase.
    """
    return text.upper()


def to_lower(text: str) -> str:
    """Convert text to lowercase.

    Args:
        text: The input text.

    Returns:
        The text in lowercase.
    """
    return text.lower()


def to_title(text: str) -> str:
    """Convert text to title case.

    Args:
        text: The input text.

    Returns:
        The text in title case.
    """
    return text.title()


def is_palindrome(text: str) -> bool:
    """Check if the text is a palindrome (ignoring case and non-alphanumeric).

    Args:
        text: The input text.

    Returns:
        True if the text is a palindrome, False otherwise.
    """
    # Normalize: remove non-alphanumeric and convert to lower case
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def random_string(length: int = 16, use_upper: bool = True, use_lower: bool = True, use_digits: bool = True, use_special: bool = False) -> str:
    """Generate a random string.

    Args:
        length: Length of the string.
        use_upper: Include uppercase letters.
        use_lower: Include lowercase letters.
        use_digits: Include digits.
        use_special: Include special characters.

    Returns:
        A random string.
    """
    import random
    import string

    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(random.choice(characters) for _ in range(length))