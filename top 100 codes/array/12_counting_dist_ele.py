def count_distinct_elements(arr):
    distinct_count = 0
    visited_elements = {} # Using a dictionary to simulate set behavior

    for element in arr:
        if element not in visited_elements:
            visited_elements[element] = True
            distinct_count += 1

    return distinct_count

# Example usage
arr = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 8]
result = count_distinct_elements(arr)
print("Distinct elements:", result)
