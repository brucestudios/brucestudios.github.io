import re

def slugify(text: str) -> str:
    """Convert a string to a slug: lowercase, alphanumeric plus hyphens."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text

def truncate(text: str, length: int, suffix: str = '...') -> str:
    """Truncate text to at most length characters, adding suffix if truncated."""
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix

def capitalize(text: str) -> str:
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())