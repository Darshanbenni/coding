def toggle_characters(input_string):
    toggled_string = ""
    for char in input_string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char
    return toggled_string

# Input string from the user
string = input("Enter a string: ")

# Call the function to toggle characters
toggled_string = toggle_characters(string)

print(f"The toggled string is: {toggled_string}")
