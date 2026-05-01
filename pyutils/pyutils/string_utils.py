import re
from typing import Union


def slugify(text: Union[str, bytes], separator: str = '-') -> str:
    """
    Convert a string to a URL-friendly slug.

    Args:
        text: The string to slugify.
        separator: The separator to use between words (default: '-').

    Returns:
        A slugified string.
    """
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    # Convert to lowercase
    text = text.lower()
    # Remove non-alphanumeric characters (except spaces and hyphens)
    text = re.sub(r'[^\w\s-]', '', text).strip()
    # Replace spaces and multiple hyphens with the separator
    text = re.sub(r'[-\s]+', separator, text)
    return text


def is_valid_email(email: str) -> bool:
    """
    Check if a string is a valid email address.

    Args:
        email: The string to check.

    Returns:
        True if the string is a valid email address, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def truncate(text: str, length: int, suffix: str = '...') -> str:
    """
    Truncate a string to a given length, adding a suffix if truncated.

    Args:
        text: The string to truncate.
        length: The maximum length of the returned string.
        suffix: The suffix to add if the string is truncated (default: '...').

    Returns:
        The truncated string.
    """
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def camel_to_snake(text: str) -> str:
    """
    Convert a camelCase string to snake_case.

    Args:
        text: The camelCase string to convert.

    Returns:
        A snake_case string.
    """
    # Insert an underscore before each uppercase letter (except the first) and convert to lowercase
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


def snake_to_camel(text: str) -> str:
    """
    Convert a snake_case string to camelCase.

    Args:
        text: The snake_case string to convert.

    Returns:
        A camelCase string.
    """
    components = text.split('_')
    # We capitalize the first letter of each component except the first one
    return components[0] + ''.join(x.title() for x in components[1:])


def pluralize(word: str, count: int = None) -> str:
    """
    Pluralize a word based on count.

    Args:
        word: The word to pluralize.
        count: The count to determine pluralization (if None, returns plural form).

    Returns:
        The pluralized word if count is not 1 (or count is None), otherwise the singular word.
    """
    if count is not None and count == 1:
        return word
    # Simple pluralization rules (for demonstration; consider using a library for production)
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    else:
        return word + 's'