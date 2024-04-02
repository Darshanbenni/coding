def replace_with_rank(arr):
    sorted_arr = sorted(arr)
    rank_dict = {}

    for rank, value in enumerate(sorted_arr):
        rank_dict[value] = rank + 1
    
    result = []
    for value in arr:
        result.append(rank_dict[value])
    
    return result

# Example input: array of numbers
arr = [10, 5, 8, 3, 1]

ranked_arr = replace_with_rank(arr)
print("Array with Ranks:", ranked_arr)
