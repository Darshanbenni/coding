def calculate_character_frequency(input_string):
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

# Input string from the user
string = input("Enter a string: ")

# Call the function to calculate character frequency
result = calculate_character_frequency(string)

# Print the character frequency
for char, count in result.items():
    print(f"'{char}' appears {count} times.")
