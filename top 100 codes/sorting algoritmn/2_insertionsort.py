def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Sorted array is:", arr)



# Insertion sort is another simple sorting algorithm that builds the 
# final sorted array one item at a time. It iterates through the input list,
# removing one element at a time and finding the correct position to insert it in the sorted part of the list.
# Here's a Python program that implements the insertion sort algorithm: