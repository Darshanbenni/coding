def capitalize_first_last_alternative(input_string):
    words = input_string.split()
    modified_words = []

    for word in words:
        modified_word = ""
        for i in range(len(word)):
            if i == 0 or i == len(word) - 1:
                modified_word += word[i].upper()
            else:
                modified_word += word[i]
        modified_words.append(modified_word)

    return " ".join(modified_words)

# Input string from the user
string = input("Enter a string: ")

# Call the alternative function to capitalize first and last letters of each word
result = capitalize_first_last_alternative(string)

print(f"The modified string is: {result}")
