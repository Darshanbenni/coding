def sum_min_abs_diff(arr):
    arr.sort()
    n = len(arr)
    total_sum = 0
    
    for i in range(1, n):
        total_sum += abs(arr[i] - arr[i - 1])
    
    return total_sum

# Example usage
array = [4, 2, 1, 3]
result = sum_min_abs_diff(array)
print("Sum of Minimum Absolute Differences:", result)
