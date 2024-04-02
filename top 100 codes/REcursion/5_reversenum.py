def reverse_number(number):
    # Base case: if the number has only one digit or is 0, return it as is
    if number < 10:
        return number
    
    # Recursive case: reverse the number by recursively reversing its digits
    last_digit = number % 10
    remaining_number = number // 10
    reversed_number = reverse_number(remaining_number)
    
    # Combine the reversed_number with the last_digit to form the final result
    return int(str(last_digit) + str(reversed_number))

# Example usage:
num = 12345
reversed_num = reverse_number(num)
print(f"Original number: {num}")
print(f"Reversed number: {reversed_num}")
