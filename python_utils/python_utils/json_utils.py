"""JSON utility functions."""

import json
from typing import Any, Union, Dict, List
from pathlib import Path

def load_json(file_path: Union[str, Path]) -> Any:
    """Load JSON data from a file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Parsed JSON data
        
    Raises:
        FileNotFoundError: If file does not exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    path_obj = Path(file_path)
    with path_obj.open('r', encoding='utf-8') as f:
        return json.load(f)

def save_json(
    data: Any, 
    file_path: Union[str, Path], 
    indent: int = 2, 
    ensure_ascii: bool = False
) -> None:
    """Save data as JSON to a file.
    
    Args:
        data: Data to serialize as JSON
        file_path: Path to output JSON file
        indent: Indentation level (default: 2)
        ensure_ascii: Whether to escape non-ASCII characters (default: False)
        
    Example:
        >>> save_json({"name": "John", "age": 30}, "user.json")
    """
    path_obj = Path(file_path)
    # Ensure parent directory exists
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    with path_obj.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)

def pretty_print_json(data: Any, indent: int = 2) -> str:
    """Pretty print JSON data as a formatted string.
    
    Args:
        data: Data to format as JSON
        indent: Indentation level (default: 2)
        
    Returns:
        Formatted JSON string
        
    Example:
        >>> pretty_print_json({"name": "John"})
        '{\\n  "name": "John"\\n}'
    """
    return json.dumps(data, indent=indent, ensure_ascii=False)

def merge_json(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple dictionaries, with later ones overriding earlier ones.
    
    Args:
        *dicts: Dictionaries to merge
        
    Returns:
        Merged dictionary
        
    Example:
        >>> merge_json({"a": 1, "b": 2}, {"b": 3, "c": 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result

def get_nested_value(data: Dict[str, Any], key_path: str, default: Any = None) -> Any:
    """Get a nested value from a dictionary using dot notation.
    
    Args:
        data: Dictionary to search
        key_path: Dot-separated path to the value (e.g., "user.address.street")
        default: Value to return if path not found
        
    Returns:
        Value at the path or default if not found
        
    Example:
        >>> data = {"user": {"address": {"street": "Main St"}}}
        >>> get_nested_value(data, "user.address.street")
        'Main St'
        >>> get_nested_value(data, "user.phone", "N/A")
        'N/A'
    """
    keys = key_path.split('.')
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, TypeError):
        return default

def set_nested_value(data: Dict[str, Any], key_path: str, value: Any) -> None:
    """Set a nested value in a dictionary using dot notation.
    
    Args:
        data: Dictionary to modify
        key_path: Dot-separated path to the value
        value: Value to set
        
    Example:
        >>> data = {}
        >>> set_nested_value(data, "user.address.street", "Main St")
        >>> data
        {'user': {'address': {'street': 'Main St'}}}
    """
    keys = key_path.split('.')
    current = data
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value