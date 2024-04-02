def calculate_frequency(arr):
    frequency = {}
    
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    return frequency

# Example usage
array = [1, 2, 3, 4, 2, 3, 1, 4, 5, 1]
frequency = calculate_frequency(array)
for element, count in frequency.items():
    print(f"Element {element} occurs {count} times.")
