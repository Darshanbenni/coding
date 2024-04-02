def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Input string from the user
string = input("Enter a string: ")

# Call the function to count vowels
vowel_count = count_vowels(string)

print(f"The number of vowels in the string is: {vowel_count}")
