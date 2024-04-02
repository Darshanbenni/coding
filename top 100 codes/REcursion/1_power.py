def power(x, n):
    # Base case: If n is 0, the result is 1.
    if n == 0:
        return 1
    # Recursive case: Compute x^(n-1) and multiply it by x.
    else:
        return x * power(x, n - 1)

# Example usage:
base = 2
exponent = 3
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
