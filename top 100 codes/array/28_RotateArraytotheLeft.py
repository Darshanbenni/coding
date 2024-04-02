def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    
    rotated_arr = []
    for i in range(n):
        rotated_arr.append(arr[(i + k) % n])
    
    return rotated_arr

# Example input: array of numbers and rotation value k
arr = [1, 2, 3, 4, 5]
k = 2

rotated_left = rotate_left(arr, k)
print("Array Rotated to the Left:", rotated_left)
