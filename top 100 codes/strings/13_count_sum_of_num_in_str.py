def sum_of_numbers(input_string):
    current_number = ""
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            total_sum += int(current_number)
            current_number = ""

    if current_number:
        total_sum += int(current_number)

    return total_sum

# Input string from the user
string = input("Enter a string with numbers: ")

# Call the function to calculate the sum of numbers
result = sum_of_numbers(string)

print(f"The sum of numbers in the string is: {result}")


'''#take user input
String = "Daya123Ben456"
#initialize integer variable
sum1 = 0
for i in String:
    #check if values lies between range of numbers or not
    #according to ascii tale
    if ord(i) >= 48 and ord(i) <= 57:
        #convert it to integer and add
        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1))'''