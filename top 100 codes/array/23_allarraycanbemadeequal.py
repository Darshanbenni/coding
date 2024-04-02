def can_make_equal(arr):
    total_sum = 0
    n = len(arr)
    
    for num in arr:
        total_sum += num
    
    return total_sum % n == 0

# Example usage
array = [3, 6, 3, 3]
if can_make_equal(array):
    print("All numbers can be made equal.")
else:
    print("All numbers cannot be made equal.")
