"""File and directory utility functions."""

import os
import shutil
from pathlib import Path
from typing import Union, List

def ensure_dir(path: Union[str, Path]) -> Path:
    """Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path to ensure
        
    Returns:
        Path object of the directory
        
    Example:
        >>> ensure_dir("path/to/directory")
        PosixPath('path/to/directory')
    """
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj

def list_files(
    directory: Union[str, Path], 
    pattern: str = "*", 
    recursive: bool = False
) -> List[Path]:
    """List files in a directory matching a pattern.
    
    Args:
        directory: Directory to search
        pattern: Glob pattern to match (default: "*")
        recursive: Whether to search recursively
        
    Returns:
        List of Path objects matching the pattern
        
    Example:
        >>> list_files("src", "*.py", recursive=True)
        [PosixPath('src/main.py'), PosixPath('src/utils.py')]
    """
    dir_path = Path(directory)
    if recursive:
        return list(dir_path.rglob(pattern))
    else:
        return list(dir_path.glob(pattern))

def copy_file(
    src: Union[str, Path], 
    dst: Union[str, Path], 
    overwrite: bool = False
) -> Path:
    """Copy a file from source to destination.
    
    Args:
        src: Source file path
        dst: Destination file path
        overwrite: Whether to overwrite if destination exists
        
    Returns:
        Path object of the destination file
        
    Raises:
        FileExistsError: If destination exists and overwrite is False
        FileNotFoundError: If source file does not exist
    """
    src_path = Path(src)
    dst_path = Path(dst)
    
    if not src_path.is_file():
        raise FileNotFoundError(f"Source file not found: {src_path}")
    
    if dst_path.exists() and not overwrite:
        raise FileExistsError(f"Destination file exists: {dst_path}")
    
    # Ensure parent directory exists
    ensure_dir(dst_path.parent)
    
    shutil.copy2(src_path, dst_path)
    return dst_path

def get_file_size(path: Union[str, Path]) -> int:
    """Get the size of a file in bytes.
    
    Args:
        path: File path
        
    Returns:
        Size in bytes
        
    Raises:
        FileNotFoundError: If file does not exist
    """
    path_obj = Path(path)
    if not path_obj.is_file():
        raise FileNotFoundError(f"File not found: {path_obj}")
    return path_obj.stat().st_size

def is_empty_file(path: Union[str, Path]) -> bool:
    """Check if a file is empty (0 bytes).
    
    Args:
        path: File path
        
    Returns:
        True if file is empty, False otherwise
        
    Example:
        >>> is_empty_file("empty.txt")
        True
    """
    try:
        return get_file_size(path) == 0
    except FileNotFoundError:
        return True  # Consider non-existent as empty for convenience