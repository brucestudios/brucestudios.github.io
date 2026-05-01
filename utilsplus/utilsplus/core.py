def to_snake_case(s: str) -> str:
    """Convert a string to snake_case."""
    import re
    # Replace spaces and hyphens with underscores
    s = re.sub(r'[\s\-]+', '_', s)
    # Convert camelCase to snake_case
    s = re.sub(r'([a-z])([A-Z])', r'\1_\2', s)
    # Convert to lowercase
    return s.lower()


def to_camel_case(s: str) -> str:
    """Convert a string to camelCase."""
    import re
    # Replace spaces and hyphens with underscores, then split
    s = re.sub(r'[\s\-]+', '_', s)
    # Split by underscore
    parts = s.split('_')
    # Lowercase first part, capitalize rest
    return parts[0].lower() + ''.join(p.capitalize() for p in parts[1:] if p)


def read_lines(filepath: str):
    """Read all lines from a file and return as list of strings."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.rstrip('\\n') for line in f]