"""
Current Time Tool

A simple utility to get the current time in various formats and timezones.
"""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def get_current_utc_time() -> datetime:
    """
    Get the current UTC time.

    Returns:
        datetime: Current time in UTC with timezone info.
    """
    return datetime.now(timezone.utc)


def get_current_time_in_timezone(tz_name: str) -> datetime:
    """
    Get the current time in a specified timezone.

    Args:
        tz_name (str): Timezone name (e.g., 'America/New_York', 'Asia/Shanghai').

    Returns:
        datetime: Current time in the specified timezone with timezone info.

    Raises:
        ZoneInfoNotFoundError: If the timezone name is not recognized.
    """
    return datetime.now(ZoneInfo(tz_name))


def get_current_timestamp() -> float:
    """
    Get the current UTC timestamp.

    Returns:
        float: Seconds since the Unix epoch.
    """
    return datetime.now().timestamp()


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S %Z%z") -> str:
    """
    Format a datetime object as a string.

    Args:
        dt (datetime): Datetime to format.
        fmt (str): Format string. Defaults to "%Y-%m-%d %H:%M:%S %Z%z".

    Returns:
        str: Formatted datetime string.
    """
    return dt.strftime(fmt)


if __name__ == "__main__":
    # Example usage when run as a script
    print("Current UTC time:", format_datetime(get_current_utc_time()))
    print("Current time in New York:", format_datetime(get_current_time_in_timezone("America/New_York")))
    print("Current time in Shanghai:", format_datetime(get_current_time_in_timezone("Asia/Shanghai")))
    print("Current timestamp:", get_current_timestamp())