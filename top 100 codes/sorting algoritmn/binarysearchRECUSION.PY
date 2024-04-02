def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Return the index of the target element if found
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    
    return -1  # Return -1 if the target element is not in the list

# Wrapper function for easier usage
def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

# Example usage:
arr = [11, 12, 22, 25, 64]
target = 12
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
