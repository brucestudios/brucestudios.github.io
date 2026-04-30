import os
import shutil
from pathlib import Path
from typing import List, Union


def safe_write(file_path: Union[str, Path], content: str, encoding: str = 'utf-8') -> None:
    """
    Safely write content to a file, creating parent directories if they don't exist.

    Args:
        file_path: Path to the file to write.
        content: Content to write to the file.
        encoding: Encoding to use (default: 'utf-8').
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)


def batch_rename(directory: Union[str, Path], pattern: str = '*', 
                 prefix: str = '', suffix: str = '', 
                 rename_func: callable = None) -> List[Path]:
    """
    Batch rename files in a directory matching a pattern.

    Args:
        directory: Directory to search for files.
        pattern: Glob pattern to match files (default: '*').
        prefix: String to prepend to each filename.
        suffix: String to append to each filename (before extension).
        rename_func: Optional function to compute new name from old name.
                    If provided, prefix and suffix are ignored.

    Returns:
        List of Path objects for the renamed files.
    """
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise ValueError(f"{directory} is not a valid directory")

    renamed_files = []
    for file_path in dir_path.glob(pattern):
        if file_path.is_file():
            if rename_func:
                new_name = rename_func(file_path.name)
            else:
                stem = file_path.stem
                suffix_part = f'{suffix}{file_path.suffix}' if suffix else file_path.suffix
                new_name = f'{prefix}{stem}{suffix_part}'
            
            new_path = file_path.with_name(new_name)
            # Avoid overwriting existing files
            counter = 1
            while new_path.exists():
                if rename_func:
                    # If using rename_func, we need to handle conflicts differently
                    # For simplicity, we'll append a counter
                    base, ext = os.path.splitext(new_name)
                    new_name = f'{base}_{counter}{ext}'
                else:
                    base, ext = os.path.splitext(new_name)
                    new_name = f'{base}_{counter}{ext}'
                new_path = file_path.with_name(new_name)
                counter += 1
            
            shutil.move(str(file_path), str(new_path))
            renamed_files.append(new_path)
    
    return renamed_files


def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """
    Copy a file from src to dst, creating parent directories if needed.

    Args:
        src: Source file path.
        dst: Destination file path.
    """
    src_path = Path(src)
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, dst_path)


def move_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """
    Move a file from src to dst, creating parent directories if needed.

    Args:
        src: Source file path.
        dst: Destination file path.
    """
    src_path = Path(src)
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src_path), str(dst_path))


def delete_file(file_path: Union[str, Path]) -> None:
    """
    Delete a file if it exists.

    Args:
        file_path: Path to the file to delete.
    """
    path = Path(file_path)
    if path.is_file():
        path.unlink()
    else:
        raise FileNotFoundError(f"{file_path} is not a file or does not exist")