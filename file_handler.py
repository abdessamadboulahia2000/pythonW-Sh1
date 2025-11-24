import os

def read_file(filename):
    """Return the full content of the file, or None if the file does not exist."""
    if not os.path.exists(filename):
        return None
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename, content):
    """Overwrite the file with the provided content."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def append_to_file(filename, content):
    """Append content to the end of the file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)


def count_lines(filename):
    """Return the number of lines in the file."""
    if not os.path.exists(filename):
        return 0
    with open(filename, "r", encoding="utf-8") as file:
        return len(file.readlines())


def count_words(filename):
    """Return the number of words in the file."""
    if not os.path.exists(filename):
        return 0
    with open(filename, "r", encoding="utf-8") as file:
        return len(file.read().split())


def search_in_file(filename, keyword):
    """Return list of lines containing the keyword (case-insensitive)."""
    if not os.path.exists(filename):
        return []
    
    result = []
    keyword = keyword.lower()

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if keyword in line.lower():
                result.append(line.strip())
    return result


def file_exists(filename):
    """Return True if the file exists, otherwise False."""
    return os.path.exists(filename)


def delete_file(filename):
    """Delete the file if it exists."""
    if os.path.exists(filename):
        os.remove(filename)
