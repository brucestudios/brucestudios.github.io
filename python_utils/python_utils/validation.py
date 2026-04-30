"""Data validation utility functions."""

import re
from typing import Union

def is_email(email: str) -> bool:
    """Check if a string is a valid email address.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid email, False otherwise
        
    Example:
        >>> is_email("user@example.com")
        True
        >>> is_email("invalid-email")
        False
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_url(url: str) -> bool:
    """Check if a string is a valid URL.
    
    Args:
        url: URL to validate
        
    Returns:
        True if valid URL, False otherwise
        
    Example:
        >>> is_url("https://example.com")
        True
        >>> is_url("not-a-url")
        False
    """
    pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
    return bool(re.match(pattern, url))

def is_phone_number(phone: str, country_code: str = 'US') -> bool:
    """Check if a string is a valid phone number.
    
    Args:
        phone: Phone number to validate
        country_code: Country code for validation (currently only 'US' supported)
        
    Returns:
        True if valid phone number, False otherwise
        
    Example:
        >>> is_phone_number("555-123-4567")
        True
        >>> is_phone_number("123")
        False
    """
    if country_code == 'US':
        # US phone number pattern: optional country code, area code, and number
        pattern = r'^(\+1\s*)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
        return bool(re.match(pattern, phone))
    # For other countries, we could extend but for now return False
    return False

def is_alphanumeric(s: str) -> bool:
    """Check if a string contains only alphanumeric characters.
    
    Args:
        s: String to check
        
    Returns:
        True if only alphanumeric, False otherwise
        
    Example:
        >>> is_alphanumeric("abc123")
        True
        >>> is_alphanumeric("abc-123")
        False
    """
    return s.isalnum()

def is_strong_password(password: str) -> bool:
    """Check if a password is strong (at least 8 chars, upper, lower, digit, special).
    
    Args:
        password: Password to validate
        
    Returns:
        True if strong password, False otherwise
        
    Example:
        >>> is_strong_password("Password123!")
        True
        >>> is_strong_password("weak")
        False
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True