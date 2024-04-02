def sort_by_frequency(arr):
    # Create a dictionary to store element frequencies
    freq_dict = {}
    for element in arr:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    # Custom sorting function
    def custom_sort(item):
        return (-freq_dict[item], item)

    # Sort the array using the custom sorting function
    arr.sort(key=custom_sort)

    return arr

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = sort_by_frequency(arr)
print(sorted_arr)
