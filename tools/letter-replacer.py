# Prompt the user for a string
string = input("Enter a string: ")

# Prompt the user for the letter to replace
letter = input("Enter the letter to replace: ")

# Prompt the user for the replacement letter
replacement = input("Enter the replacement letter: ")

# Replace the specified letter with the replacement letter
string = string.replace(letter, replacement)

# Print the modified string
print("Modified string:", string)
