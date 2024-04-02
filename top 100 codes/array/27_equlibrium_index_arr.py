def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return i
        left_sum += num
    
    return -1  # If no equilibrium index is found

# Example input: array of numbers
arr = [-7, 1, 5, 2, -4, 3, 100]

equilibrium_idx = equilibrium_index(arr)
if equilibrium_idx != -1:
    print(f"Equilibrium Index: {equilibrium_idx}")
else:
    print("No equilibrium index found.")
