def is_array_palindrome(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example usage
array1 = [1, 2, 3, 2, 1]


if is_array_palindrome(array1):
    print("Array 1 is a palindrome.")
else:
    print("Array 1 is not a palindrome.")
