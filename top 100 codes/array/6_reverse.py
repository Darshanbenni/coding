def reverse_arr(A, start, end):
    
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    print(A)
    

A = [10,24,4,134,34]
reverse_arr(A, 0, 4)