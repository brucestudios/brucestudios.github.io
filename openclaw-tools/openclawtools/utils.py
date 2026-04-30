"""Utility functions for OpenClaw."""

def hello_world(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: The name to greet.
        
    Returns:
        A greeting string.
    """
    return f"Hello, {name}! Welcome to OpenClaw Tools."

def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        The sum of a and b.
    """
    return a + b

def is_even(number: int) -> bool:
    """Check if a number is even.
    
    Args:
        number: The number to check.
        
    Returns:
        True if the number is even, False otherwise.
    """
    return number % 2 == 0