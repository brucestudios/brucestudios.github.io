"""
Handy Python Utilities
A collection of useful utility functions for everyday Python tasks.
"""

import os
import json
import csv
import shutil
from pathlib import Path
from typing import Any, Dict, List, Union, Optional
import datetime
import hashlib


def ensure_dir(path: Union[str, Path]) -> Path:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path to ensure exists
        
    Returns:
        Path object of the directory
    """
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj


def read_json(file_path: Union[str, Path]) -> Any:
    """
    Read and parse a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Parsed JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file is not valid JSON
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data: Any, file_path: Union[str, Path], indent: int = 2) -> None:
    """
    Write data to a JSON file.
    
    Args:
        data: Data to write to file
        file_path: Path to the JSON file
        indent: Indentation level for pretty printing (default: 2)
    """
    path_obj = Path(file_path)
    ensure_dir(path_obj.parent)
    
    with open(path_obj, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def read_csv(file_path: Union[str, Path], has_header: bool = True) -> List[Dict[str, Any]]:
    """
    Read a CSV file and return list of dictionaries.
    
    Args:
        file_path: Path to the CSV file
        has_header: Whether the CSV has a header row (default: True)
        
    Returns:
        List of dictionaries representing CSV rows
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        if has_header:
            reader = csv.DictReader(f)
            return list(reader)
        else:
            reader = csv.reader(f)
            return [row for row in reader]


def write_csv(data: List[Dict[str, Any]], file_path: Union[str, Path]) -> None:
    """
    Write list of dictionaries to a CSV file.
    
    Args:
        data: List of dictionaries to write
        file_path: Path to the CSV file
    """
    if not data:
        # Write empty file with no headers
        Path(file_path).touch()
        return
        
    path_obj = Path(file_path)
    ensure_dir(path_obj.parent)
    
    with open(path_obj, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def backup_file(file_path: Union[str, Path], backup_dir: Optional[Union[str, Path]] = None) -> Path:
    """
    Create a timestamped backup of a file.
    
    Args:
        file_path: Path to file to backup
        backup_dir: Directory to store backup (defaults to same directory as file)
        
    Returns:
        Path to the backup file
        
    Raises:
        FileNotFoundError: If source file doesn't exist
    """
    src_path = Path(file_path)
    if not src_path.exists():
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    if backup_dir is None:
        backup_dir = src_path.parent
    else:
        backup_dir = Path(backup_dir)
        ensure_dir(backup_dir)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{src_path.stem}_{timestamp}{src_path.suffix}"
    backup_path = backup_dir / backup_name
    
    shutil.copy2(src_path, backup_path)
    return backup_path


def get_file_hash(file_path: Union[str, Path], algorithm: str = 'sha256') -> str:
    """
    Calculate hash of a file.
    
    Args:
        file_path: Path to the file
        algorithm: Hash algorithm to use (default: 'sha256')
        
    Returns:
        Hexadecimal hash string
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If unsupported algorithm is specified
    """
    hash_obj = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()


def flatten_dict(nested_dict: Dict[str, Any], separator: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary using dot notation.
    
    Args:
        nested_dict: Dictionary to flatten
        separator: Separator to use between keys (default: '.')
        
    Returns:
        Flattened dictionary
    """
    def _flatten(obj, parent_key=''):
        items = []
        for k, v in obj.items():
            new_key = f"{parent_key}{separator}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(_flatten(v, new_key).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    return _flatten(nested_dict)


def unflatten_dict(flat_dict: Dict[str, Any], separator: str = '.') -> Dict[str, Any]:
    """
    Unflatten a dictionary from dot notation.
    
    Args:
        flat_dict: Flattened dictionary
        separator: Separator used between keys (default: '.')
        
    Returns:
        Nested dictionary
    """
    result = {}
    for key, value in flat_dict.items():
        parts = key.split(separator)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        lst: List to chunk
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")
    
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def merge_dicts(*dicts: Dict[str, Any], deep: bool = False) -> Dict[str, Any]:
    """
    Merge multiple dictionaries.
    
    Args:
        *dicts: Dictionaries to merge
        deep: Whether to perform deep merge (default: False)
        
    Returns:
        Merged dictionary
    """
    if not dicts:
        return {}
    
    if not deep:
        result = {}
        for d in dicts:
            result.update(d)
        return result
    
    # Deep merge
    def _deep_merge(a, b):
        result = a.copy()
        for k, v in b.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = _deep_merge(result[k], v)
            else:
                result[k] = v
        return result
    
    result = {}
    for d in dicts:
        result = _deep_merge(result, d)
    return result


def safe_get(nested_dict: Dict[str, Any], key_path: str, default: Any = None, separator: str = '.') -> Any:
    """
    Safely get a value from a nested dictionary using dot notation.
    
    Args:
        nested_dict: Dictionary to search
        key_path: Dot-separated path to the value (e.g., 'a.b.c')
        default: Default value to return if path not found
        separator: Separator used in key_path (default: '.')
        
    Returns:
        Value at the path or default if not found
    """
    keys = key_path.split(separator)
    current = nested_dict
    
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default


if __name__ == "__main__":
    # Simple demo when run directly
    print("Handy Python Utilities")
    print("======================")
    print("This module provides utility functions for everyday Python tasks.")
    print("Import and use the functions you need:")
    print("  from utils import ensure_dir, read_json, write_json, etc.")