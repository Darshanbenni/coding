def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    without_vowels = ""

    for char in input_string:
        if char not in vowels:
            without_vowels += char

    return without_vowels

# Input string from the user
string = input("Enter a string:")

# Call the function to remove vowels
result = remove_vowels(string)

print(f"The string without vowels is: {result}")
