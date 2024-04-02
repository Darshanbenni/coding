def maxSubarrayProduct(arr, n):
 
    # Initializing result
    result = arr[0]
 
    for i in range(n):
     
        mul = arr[i]
       
        # traversing in current subarray
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]
         
        # updating the result for (n-1)th index.
        result = max(result, mul)
     
    return result
 
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxSubarrayProduct(arr, n))



'''def max_product_subarray(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    max_global = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == 0:
            max_product = min_product = 1
            continue
        
        temp = max_product
        max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
        min_product = min(nums[i], temp * nums[i], min_product * nums[i])
        
        max_global = max(max_global, max_product)
    
    return max_global

# Example input: array of numbers
nums = [2, 3, -2, 4, -1]

result = max_product_subarray(nums)
print("Maximum Product Sub-array:", result)'''
