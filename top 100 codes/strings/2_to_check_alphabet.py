def check_alphabet(char):
    # Convert the character to its ASCII value
    ascii_value = ord(char)

    # Check if the ASCII value falls within the range of lowercase or uppercase alphabets
    if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
        return "Alphabet"
    else:
        return "Not an alphabet"

# Input character from the user
character = input("Enter a character: ")

# Call the function and display the result
result = check_alphabet(character)
print(f"The character '{character}' is {result}.")
