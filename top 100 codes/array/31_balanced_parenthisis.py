def is_balanced(expression):
    stack = []
    
    # Define a dictionary to map closing parentheses to their corresponding opening parentheses
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening parenthesis, push it onto the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing parenthesis
        elif char in ')}]':
            # Check if the stack is empty or if the top of the stack doesn't match the corresponding opening parenthesis
            if not stack or stack.pop() != brackets[char]:
                return False
    
    # If the stack is empty, the expression is balanced
    return not stack

# Example usage:
expression = "{[()]}"
if is_balanced(expression):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")
