def min_scalar_product(vector1, vector2):
    n = len(vector1)
    
    # Pair the elements and calculate the scalar product
    scalar_product = sum(vector1[i] * vector2[i] for i in range(n))
    
    return scalar_product

# Example usage
vector1 = [1, 3, -5]
vector2 = [-2, 4, 1]
result = min_scalar_product(vector1, vector2)
print("Minimum Scalar Product:", result)
