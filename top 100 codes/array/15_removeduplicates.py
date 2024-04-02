def remove_duplicates(arr):
    unique_elements = []
    
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    
    return unique_elements

# Example usage
arr = [4, 2, 5, 2, 7, 8, 8, 9, 4]
result = remove_duplicates(arr)
print("Array after removing duplicates:", result)
