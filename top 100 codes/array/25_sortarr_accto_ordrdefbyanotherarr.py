def custom_sort(arr, order):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            # Compare indices of arr[j] and arr[j+1] in the order array
            if order.index(arr[j]) > order.index(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    
    return arr

# Example input: arrays of numbers and order
arr = [10, 5, 8, 3, 1]
order = [5, 10, 3, 8, 1]

sorted_arr = custom_sort(arr, order)
print("Sorted Array According to Order:", sorted_arr)

'''Certainly! The program is aimed at sorting an array (`arr`) according to a specific order defined by another
array (`order`) without using built-in functions. Here's a breakdown of the program:

1. Define the function `custom_sort(arr, order)` that takes two arrays as arguments.

2. Get the length of the array `arr` and store it in the variable `n`.

3. Implement the Bubble Sort algorithm to sort the array `arr` according to the order defined in the array `order`.

4. The outer loop (`for i in range(n - 1)`) runs through the array `arr` to ensure that all elements are correctly positioned.

5. The inner loop (`for j in range(0, n - i - 1)`) iterates through adjacent pairs of elements in the array `arr`.

6. Inside the inner loop, the program compares the indices of the current element (`arr[j]`) 
and the next element (`arr[j+1]`) in the `order` array. If the index of `arr[j]` in the `order`
array is greater than the index of `arr[j+1]`, it means that `arr[j]` should come after `arr[j+1]` 
in the sorted order. Therefore, the elements are swapped.

7. After the inner loop finishes, the program checks if any swaps were made in that iteration.
If no swaps were made, it means that the array is already sorted according to the order, and the 
loop can be terminated early using the `break` statement.

8. Finally, the sorted `arr` is returned.

9. The example input arrays `arr` and `order` are provided, and the `custom_sort` function is called with these arrays.

10. The sorted array is printed using `print("Sorted Array According to Order:", sorted_arr)`.

The main idea of the program is to modify the sorting comparison in the Bubble Sort algorithm to consider the order 
defined by the `order` array. Elements are compared and swapped based on their positions in the `order` array rather 
than their numerical values. This way, the final sorted array respects the desired order.'''