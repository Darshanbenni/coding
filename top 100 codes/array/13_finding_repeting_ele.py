def find_repeating_elements(arr):
    repeating_elements = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in repeating_elements:
                repeating_elements.append(arr[i])

    return repeating_elements

# Example usage
arr = [4, 2, 5, 2, 7, 8, 8, 9, 4]
result = find_repeating_elements(arr)
print("Repeating elements:", result)
