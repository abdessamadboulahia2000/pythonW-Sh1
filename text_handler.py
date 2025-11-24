import string

def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (case-insensitive).
    """
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]


def count_vowels(text):
    """Return the number of vowels in the text."""
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


def reverse_text(text: str) -> str:
    """
    Return the reversed version of the input string.
    """
    return text[::-1]


def remove_punctuation(text):
    """Return the text with all punctuation removed."""
    return text.translate(str.maketrans("", "", string.punctuation))


def capitalize_words(text):
    """Return the text with each word capitalized."""
    return text.title()


def count_words(text: str) -> int:
    """
    Count the number of words in a given text.
    """
    words = text.split()
    return len(words)


def unique_words(text):
    """Return a set of unique words in the text."""
    return set(text.lower().split())
