def keep_only_alphabets(input_string):
    alphabet_string = ""

    for char in input_string:
        if char.isalpha():
            alphabet_string += char

    return alphabet_string

# Input string from the user
string = input("Enter a string: ")

# Call the function to keep only alphabets
result = keep_only_alphabets(string)

print(f"The string with only alphabets is: {result}")

#take user input
''' String1 = "#Justice!For@Chutki123"
#initialize empty String
String2 = ''
for i in String1:
    #check for alphabets
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        #concatenate to empty string
        String2+=i
print('Alphabets in string are :' + String2)'''