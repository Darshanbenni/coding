def custom_sort(arr):
    n = len(arr)
    mid = n // 2

    # Sort the first half in ascending order using bubble sort
    for i in range(mid):
        for j in range(mid - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Sort the second half in descending order using bubble sort
    for i in range(mid, n - 1):
        for j in range(mid, n - i + mid - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage
arr = [7, 2, 5, 9, 1, 8]
sorted_array = custom_sort(arr)
print(sorted_array)
