String = "prepinsta"
for i in String:
    #initialize a count variable
    count = 0
    for j in String:
        #check for repeated characters
        if i == j:
            count+=1
        #if character is found more than 1 time
        #brerak the loop
        if count > 1:
            break
    #print for nonrepeating characters
    if count == 1:
        print(i,end = " ")
        
        
'''def find_non_repeating_characters(input_string):
    character_count = {}
    non_repeating_characters = []

    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    for char, count in character_count.items():
        if count == 1:
            non_repeating_characters.append(char)

    return non_repeating_characters

# Input string from the user
string = input("Enter a string: ")

# Call the function to find non-repeating characters
result = find_non_repeating_characters(string)

print("Non-repeating characters in the string:", ", ".join(result))
'''