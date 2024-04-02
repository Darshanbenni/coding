def find_non_repeating_elements(arr):
    non_repeating_elements = []

    for element in arr:
        if arr.count(element) == 1 and element not in non_repeating_elements:
            non_repeating_elements.append(element)

    return non_repeating_elements

# Example usage
arr = [4, 2, 5, 2, 7, 8, 8, 9, 4]
result = find_non_repeating_elements(arr)
print("Non-repeating elements:", result)
