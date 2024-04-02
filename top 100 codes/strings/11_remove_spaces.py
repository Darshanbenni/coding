def remove_spaces(input_string):
    space_removed_string = ""
    for char in input_string:
        if char != ' ':
            space_removed_string += char
    return space_removed_string

# Input string from the user
string = input("Enter a string: ")

# Call the function to remove spaces
result = remove_spaces(string)

print(f"The string with spaces removed is: {result}")


'''def remove_spaces(input_string):
    space_removed_string = input_string.replace(" ", "")
    return space_removed_string

# Input string from the user
string = input("Enter a string: ")

# Call the function to remove spaces
result = remove_spaces(string)

print(f"The string with spaces removed is: {result}")
'''