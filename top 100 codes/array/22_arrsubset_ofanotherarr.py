def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
    return True

# Example usage
array1 = [1, 2, 3]
array2 = [5, 1, 2, 3, 4]
if is_subset(array1, array2):
    print("Array1 is a subset of Array2.")
else:
    print("Array1 is not a subset of Array2.")
    
    
#to return the subset
# def find_subset(arr1, arr2):
#     subset = []
#     for element in arr1:
#         if element not in arr2:
#             return None
#         subset.append(element)
#     return subset

# # Example usage
# array1 = [1, 2, 3]
# array2 = [5, 1, 2, 3, 4]
# subset = find_subset(array1, array2)

# if subset is not None:
#     print("Array1 is a subset of Array2:", subset)
# else:
#     print("Array1 is not a subset of Array2.")
