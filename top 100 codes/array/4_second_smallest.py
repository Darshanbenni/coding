arr = [10,24,45,6,7,134,34]

first = arr[0]
second = arr[1]

for i in range(len(arr)):
    if arr[i] < first:
        first = arr[i]
        
for i in range(len(arr)):
    if arr[i] != first and arr[i] < second:
        second = arr[i]
        
print(second)