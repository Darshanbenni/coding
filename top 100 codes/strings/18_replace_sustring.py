string=input("Enter String :\n")
str1=input("Enter substring which has to be replaced :\n")
str2=input("Enter substring with which str1 has to be replaced :\n")
string=string.replace(str1,str2)
print("String after replacement")
print(string)



'''
def replace_substring(input_string, old_substring, new_substring):
    result = input_string.replace(old_substring, new_substring)
    return result

# Input string from the user
string = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")

# Call the function to replace the substring
result = replace_substring(string, old_substring, new_substring)

print(f"The modified string is: {result}")
'''