def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Input string from the user
string = input("Enter a string: ")

# Call the function to reverse the string
reversed_result = reverse_string(string)

print(f"The reversed string is: {reversed_result}")

'''Certainly! The provided program reverses a given string without using any built-in functions. 
Here's a step-by-step explanation of how it works:

1. The program defines a function named `reverse_string` that takes an `input_string` as an argument.

2. Inside the function, there's an empty string called `reversed_string`, which will store the reversed 
version of the input string.

3. The program enters a loop that iterates over each character (`char`) in the `input_string`.

4. For each character in the input string:
   - The program concatenates (appends) the current character `char` to the beginning of the `reversed_string`. 
   This is done by using the `char + reversed_string` operation.
   - By doing this, the characters are added to the new string in reverse order, effectively reversing the original string.

5. After the loop completes, the `reversed_string` will contain the reversed version of the input string.

6. The `reverse_string` function returns the `reversed_string`.

7. The main part of the program takes an input string from the user.

8. It calls the `reverse_string` function, passing the user-provided string as an argument. 
The returned value (reversed string) is stored in the `reversed_result` variable.

9. Finally, the program prints out the reversed string using the `reversed_result` variable.

This approach manually constructs the reversed string by iterating over each character of the input 
string and adding them to the beginning of the new string. This effectively achieves the same result as using 
slicing (`[::-1]`) to reverse the string.'''