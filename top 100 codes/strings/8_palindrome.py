def is_palindrome(input_string):
    length = len(input_string)
    for i in range(length // 2):
        if input_string[i] != input_string[length - i - 1]:
            return False
    return True

# Input string from the user
string = input("Enter a string: ")

# Call the function to check if the string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
