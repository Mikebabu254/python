# Request user input
char = input("Enter a character: ").lower()

# Check if it's a vowel or consonant
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")
