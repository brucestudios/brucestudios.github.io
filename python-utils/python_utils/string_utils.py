"""String utility functions."""

def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the text.
    
    Args:
        text: Input string
        
    Returns:
        String with each word capitalized
    """
    return ' '.join(word.capitalize() for word in text.split())

def remove_extra_spaces(text: str) -> str:
    """Remove extra spaces from the text.
    
    Args:
        text: Input string
        
    Returns:
        String with single spaces between words and no leading/trailing spaces
    """
    return ' '.join(text.split())

def reverse_string(text: str) -> str:
    """Reverse the input string.
    
    Args:
        text: Input string
        
    Returns:
        Reversed string
    """
    return text[::-1]