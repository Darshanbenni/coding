def max_scalar_product(vector1, vector2):
    n = len(vector1)
    scalar_product = 0
    
    for _ in range(n):
        max1 = max(vector1)
        max2 = max(vector2)
        
        scalar_product += max1 * max2
        
        vector1.remove(max1)
        vector2.remove(max2)
    
    return scalar_product

# Example usage
vector1 = [1, 3, -5]
vector2 = [-2, 4, 1]
result = max_scalar_product(vector1, vector2)
print("Maximum Scalar Product:", result)






''' def max_scalar_product(arr1, arr2):
    # Sort the arrays in descending order
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    
    # Calculate the maximum scalar product
    max_product = 0
    for i in range(len(arr1)):
        max_product += arr1[i] * arr2[i]
    
    return max_product

# Read input arrays from the user
n = int(input("Enter the number of elements: "))
arr1 = []
arr2 = []

print("Enter elements for the first array:")
for _ in range(n):
    arr1.append(int(input())) '''

# print("Enter elements for the second array:")
# for _ in range(n):
#     arr2.append(int(input()))

# # Calculate and print the maximum scalar product
# result = max_scalar_product(arr1, arr2)
# print("Maximum Scalar Product:", result)'''
