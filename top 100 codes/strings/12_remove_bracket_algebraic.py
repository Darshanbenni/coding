def remove_brackets(expression):
    without_brackets = ""
    inside_brackets = ""

    for char in expression:
        if char == '(':
            inside_brackets = ""
        elif char == ')':
            without_brackets += inside_brackets
            inside_brackets = ""
        else:
            inside_brackets += char
    
    without_brackets += inside_brackets
    return without_brackets

# Input algebraic expression from the user
expression = input("Enter an algebraic expression: ")

# Call the function to remove brackets
result = remove_brackets(expression)

print(f"The expression without brackets is: {result}")
