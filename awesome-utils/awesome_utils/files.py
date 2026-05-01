"""File and directory utility functions."""

import os
from pathlib import Path
from typing import Union

def ensure_dir(path: Union[str, Path]) -> Path:
    """Ensure that a directory exists, creating it if necessary.
    
    Args:
        path: The directory path to ensure.
        
    Returns:
        Path object of the directory.
    """
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj

def list_files(directory: Union[str, Path], pattern: str = "*") -> list:
    """List files in a directory matching a pattern.
    
    Args:
        directory: The directory to search.
        pattern: Glob pattern for matching files.
        
    Returns:
        List of Path objects for matching files.
    """
    return list(Path(directory).glob(pattern))

def read_text(file_path: Union[str, Path], encoding: str = "utf-8") -> str:
    """Read text content from a file.
    
    Args:
        file_path: Path to the file.
        encoding: Text encoding (default: utf-8).
        
    Returns:
        The file content as a string.
    """
    return Path(file_path).read_text(encoding=encoding)

def write_text(file_path: Union[str, Path], content: str, encoding: str = "utf-8") -> None:
    """Write text content to a file.
    
    Args:
        file_path: Path to the file.
        content: The text content to write.
        encoding: Text encoding (default: utf-8).
    """
    Path(file_path).write_text(content, encoding=encoding)