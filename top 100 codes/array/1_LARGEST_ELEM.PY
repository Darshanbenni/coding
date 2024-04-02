arr = [10,24,4,134,34]

max_ele = arr[0]

for i in range(len(arr)):
    
   if arr[i] > max_ele:
        max_ele = arr[i]
print(max_ele)