# Open the text file in read mode
file_name = "text.txt"  # Replace with the actual file name
with open(file_name, "r") as file:
    text = file.read()

# Count characters
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Display character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")
