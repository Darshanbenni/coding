def are_anagrams(string1, string2):
    if len(string1) != len(string2):
        return False

    char_count = {}

    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    return all(value == 0 for value in char_count.values())

# Input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function to check if strings are anagrams
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")



'''# Anagram program in python
# take user input
String1 = "Listen"
String2 = "Silent"

String1 = sorted(String1.lower())
String2 = sorted(String2.lower())

print("String1 after sorting: ", String1)
print("String2 after sorting: ", String2)

# check if now strings matches
if String1 == String2:
    print('Strings are anagram')
else:
    print('Strings are not anagram')'''