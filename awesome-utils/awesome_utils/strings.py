"""String utility functions."""

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the text.
    
    Args:
        text: The input string.
        
    Returns:
        A string with each word capitalized.
    """
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text: str) -> str:
    """Reverse the input string.
    
    Args:
        text: The input string.
        
    Returns:
        The reversed string.
    """
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Check if the string is a palindrome (ignoring case and non-alphanumeric).
    
    Args:
        text: The input string.
        
    Returns:
        True if the string is a palindrome, False otherwise.
    """
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]