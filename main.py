import file_handler # type: ignore
import text_handler # type: ignore

print("===== TESTING file_handler.py =====\n")

# Test write_file
file_handler.write_file("example.txt", "Hello,\nThis is a test.\nPython is great.")

# Test read_file
print("=== File Content ===")
content = file_handler.read_file("example.txt")
print(content)

# Test append_to_file
file_handler.append_to_file("example.txt", "\nAdding a new line.")
print("\n=== After Appending ===")
print(file_handler.read_file("example.txt"))

# Test count_lines
print("\nNumber of lines:", file_handler.count_lines("example.txt"))

# Test count_words
print("Number of words:", file_handler.count_words("example.txt"))

# Test search_in_file
print("\nLines containing 'test':")
print(file_handler.search_in_file("example.txt", "test"))

# Test file_exists
print("\nDoes the file exist?", file_handler.file_exists("example.txt"))

# Test delete_file
file_handler.delete_file("example.txt")
print("File deleted.")
print("Does it still exist?", file_handler.file_exists("example.txt"))



print("\n\n===== TESTING text_handler.py =====\n")

text = "Hello world! Python is amazing, truly amazing."

# is_palindrome
print("Is 'Radar' a palindrome?", text_handler.is_palindrome("Radar"))

# count_vowels
print("Number of vowels:", text_handler.count_vowels(text))

# reverse_text
print("Reversed text:", text_handler.reverse_text("Hello World"))

# remove_punctuation
print("Without punctuation:", text_handler.remove_punctuation(text))

# capitalize_words
print("Capitalized words:", text_handler.capitalize_words(text))

# count_words
print("Word count:", text_handler.count_words("This is a simple test"))

# unique_words
print("Unique words:", text_handler.unique_words(text))
