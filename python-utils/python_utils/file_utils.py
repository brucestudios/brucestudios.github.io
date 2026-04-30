"""File utility functions."""

def read_lines(filepath: str) -> list[str]:
    """Read all lines from a file.
    
    Args:
        filepath: Path to the file
        
    Returns:
        List of lines (without newline characters)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.rstrip('\\n') for line in f]

def write_lines(filepath: str, lines: list[str]) -> None:
    """Write lines to a file.
    
    Args:
        filepath: Path to the file
        lines: List of strings to write (each will be written on its own line)
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\\n')

def file_exists(filepath: str) -> bool:
    """Check if a file exists.
    
    Args:
        filepath: Path to the file
        
    Returns:
        True if file exists, False otherwise
    """
    import os
    return os.path.isfile(filepath)