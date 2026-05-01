"""Date and time utility functions."""

from datetime import datetime, timedelta
from typing import Union

def now() -> datetime:
    """Get the current local datetime.
    
    Returns:
        Current datetime
        
    Example:
        >>> dt = now()
        >>> isinstance(dt, datetime)
        True
    """
    return datetime.now()

def utc_now() -> datetime:
    """Get the current UTC datetime.
    
    Returns:
        Current UTC datetime
    """
    return datetime.utcnow()

def format_date(dt: Union[datetime, str], fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime object as a string.
    
    Args:
        dt: datetime object or ISO format string
        fmt: Format string (default: "%Y-%m-%d %H:%M:%S")
        
    Returns:
        Formatted date string
        
    Example:
        >>> format_date(datetime(2023, 1, 1, 12, 0, 0))
        '2023-01-01 12:00:00'
    """
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.strftime(fmt)

def parse_date(date_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """Parse a string into a datetime object.
    
    Args:
        date_str: Date string to parse
        fmt: Format string (default: "%Y-%m-%d %H:%M:%S")
        
    Returns:
        Parsed datetime object
        
    Example:
        >>> parse_date("2023-01-01 12:00:00")
        datetime.datetime(2023, 1, 1, 12, 0, 0)
    """
    return datetime.strptime(date_str, fmt)

def add_days(dt: Union[datetime, str], days: int) -> datetime:
    """Add days to a datetime.
    
    Args:
        dt: datetime object or ISO format string
        days: Number of days to add (can be negative)
        
    Returns:
        New datetime object
        
    Example:
        >>> add_days(datetime(2023, 1, 1), 5)
        datetime.datetime(2023, 1, 6, 0, 0)
    """
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt + timedelta(days=days)

def add_hours(dt: Union[datetime, str], hours: int) -> datetime:
    """Add hours to a datetime.
    
    Args:
        dt: datetime object or ISO format string
        hours: Number of hours to add (can be negative)
        
    Returns:
        New datetime object
    """
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt + timedelta(hours=hours)

def is_weekday(dt: Union[datetime, str]) -> bool:
    """Check if a date is a weekday (Monday-Friday).
    
    Args:
        dt: datetime object or ISO format string
        
    Returns:
        True if weekday, False if weekend
        
    Example:
        >>> is_weekday(datetime(2023, 1, 2))  # Monday
        True
        >>> is_weekday(datetime(2023, 1, 7))  # Saturday
        False
    """
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.weekday() < 5  # Monday=0, Sunday=6

def days_between(start: Union[datetime, str], end: Union[datetime, str]) -> int:
    """Calculate the number of days between two dates.
    
    Args:
        start: Start date
        end: End date
        
    Returns:
        Number of days (can be negative if end is before start)
        
    Example:
        >>> days_between(datetime(2023, 1, 1), datetime(2023, 1, 5))
        4
    """
    if isinstance(start, str):
        start = datetime.fromisoformat(start)
    if isinstance(end, str):
        end = datetime.fromisoformat(end)
    return (end - start).days