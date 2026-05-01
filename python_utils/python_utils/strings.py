"""String utility functions."""

def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word in a string.
    
    Args:
        s: Input string
        
    Returns:
        String with each word capitalized
        
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return ' '.join(word.capitalize() for word in s.split())

def snake_to_camel(s: str) -> str:
    """Convert snake_case string to camelCase.
    
    Args:
        s: Snake case string
        
    Returns:
        Camel case string
        
    Example:
        >>> snake_to_camel("hello_world")
        'helloWorld'
    """
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(s: str) -> str:
    """Convert camelCase string to snake_case.
    
    Args:
        s: Camel case string
        
    Returns:
        Snake case string
        
    Example:
        >>> camel_to_snake("helloWorld")
        'hello_world'
    """
    import re
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

def truncate(s: str, length: int, suffix: str = '...') -> str:
    """Truncate a string to a given length, adding a suffix if truncated.
    
    Args:
        s: Input string
        length: Maximum length (including suffix)
        suffix: String to append if truncated
        
    Returns:
        Truncated string
        
    Example:
        >>> truncate("Hello world", 8)
        'Hello...'
    """
    if len(s) <= length:
        return s
    return s[:length - len(suffix)] + suffix

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (ignoring case and non-alphanumeric).
    
    Args:
        s: Input string
        
    Returns:
        True if string is palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
    """
    import re
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]