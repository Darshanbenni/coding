def swap(arr, start, end, d):
    for i in range(d):
        arr[start + i], arr[end + i] = arr[end + i], arr[start + i]

def rotate_left_block_swap(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d > n
    
    swap(arr, 0, d, d)
    
    while n - d > d:
        swap(arr, d, n - d, d)
        n -= d
    
    swap(arr, 0, n, n)

# Example input: array of numbers and rotation value d
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

rotate_left_block_swap(arr, d)
print("Array Rotated to the Left:", arr)
'''
I apologize for any confusion. Let me explain the Block-Swapping Algorithm for array rotation more clearly.

In the Block-Swapping Algorithm, we divide the array into two blocks, one with the first `d` elements and the other with the remaining elements. We then swap these two blocks to achieve the rotation.

Here's how the algorithm works:

1. **Rotate Array to the Left using Block-Swapping:**
   - Divide the array into two blocks: Block 1 with the first `d` elements and Block 2 with the remaining elements.
   - Swap the elements of Block 1 and Block 2 to achieve the rotation.

2. **Rotate Array to the Right using Block-Swapping:**
   - Divide the array into two blocks: Block 1 with the first `n - d` elements and Block 2 with the last `d` elements.
   - Swap the elements of Block 1 and Block 2 to achieve the rotation.

Let's take an example to illustrate:

**Example:**
```python
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
```

**Rotate Array to the Left:**
- Block 1: [1, 2]
- Block 2: [3, 4, 5, 6, 7]
- Swap Block 1 and Block 2: [3, 4, 5, 6, 7, 1, 2]

**Rotate Array to the Right:**
- Block 1: [1, 2, 3, 4, 5]
- Block 2: [6, 7]
- Swap Block 1 and Block 2: [6, 7, 3, 4, 5, 1, 2]

So, the main idea of blocking is to divide the array into two parts and swap them to achieve rotation.

I hope this explanation clarifies the concept of the Block-Swapping Algorithm for array rotation.'''