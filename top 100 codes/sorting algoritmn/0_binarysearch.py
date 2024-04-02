# Binary search is an efficient search algorithm for finding a target element 
# in a sorted list. It works by repeatedly dividing the list in half and comparing 
# the target element with the middle element. Here's a Python program that implements the binary search algorithm:

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Return the index of the target element if found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target element is not in the list

# Example usage:
arr = [11, 12, 22, 25, 64]
target = 12
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
