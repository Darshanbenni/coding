arr = [10,24,4,134,34]


min_ele = arr[0]

for i in range(len(arr)):
    if arr[i] < min_ele:
        min_ele = arr[i]
print(min_ele)