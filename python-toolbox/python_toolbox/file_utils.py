import os
import shutil
from pathlib import Path

def copy_file(src: str, dst: str) -> None:
    """Copy a file from src to dst."""
    shutil.copy2(src, dst)

def move_file(src: str, dst: str) -> None:
    """Move a file from src to dst."""
    shutil.move(src, dst)

def safe_delete(path: str) -> None:
    """Delete a file if it exists, without raising an error."""
    try:
        os.remove(path)
    except FileNotFoundError:
        pass