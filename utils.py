def format_filename(s: str) -> str:
    """Replace spaces with underscores and remove invalid filename characters."""
    import re
    s = s.strip().replace(' ', '_')
    return re.sub(r'[^\\w\\-.]', '', s)

def chunk_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def read_file_lines(path):
    """Read lines from a file, stripping newline characters."""
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\\n') for f in f]

if __name__ == "__main__":
    # Simple demo
    print("Testing utils:")
    print(format_filename("  hello world!  "))
    print(list(chunk_list([1,2,3,4,5,6], 3)))