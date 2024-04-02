def is_palindrome(s):
    # Helper function to check if a string is a palindrome
    return s == s[::-1]

def find_longest_palindrome(arr):
    longest_palindrome = ""
    
    for s in arr:
        if is_palindrome(s) and len(s) > len(longest_palindrome):
            longest_palindrome = s
            
    return longest_palindrome

# Example usage:
array_of_strings = ["racecar", "hello", "madam", "python", "level"]
result = find_longest_palindrome(array_of_strings)

if result:
    print("Longest palindrome:", result)
else:
    print("No palindrome found in the array.")
