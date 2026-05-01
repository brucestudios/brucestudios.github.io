"""
Data validation utilities.
"""

import re

def is_email(text: str) -> bool:
    """
    Check if the string is a valid email address.
    
    Note: This is a simple regex and may not cover all edge cases.
    For production, consider using a dedicated library like email-validator.
    
    Args:
        text: The string to check.
    
    Returns:
        True if the string looks like an email, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, text) is not None

def is_url(text: str) -> bool:
    """
    Check if the string is a valid URL.
    
    Args:
        text: The string to check.
    
    Returns:
        True if the string looks like a URL, False otherwise.
    """
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return re.match(pattern, text) is not None

def is_alpha(text: str) -> bool:
    """
    Check if the string contains only alphabetic characters.
    
    Args:
        text: The string to check.
    
    Returns:
        True if the string is alphabetic, False otherwise.
    """
    return text.isalpha()

def is_alphanumeric(text: str) -> bool:
    """
    Check if the string contains only alphanumeric characters.
    
    Args:
        text: The string to check.
    
    Returns:
        True if the string is alphanumeric, False otherwise.
    """
    return text.isalnum()