def replace_word(input_string, target_word, new_word):
    words = input_string.split()
    modified_words = []

    for word in words:
        if word == target_word:
            modified_words.append(new_word)
        else:
            modified_words.append(word)

    return " ".join(modified_words)

# Input string from the user
string = input("Enter a string: ")
target_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

# Call the function to replace the word
result = replace_word(string, target_word, new_word)

print(f"The modified string is: {result}")
