def find_symmetric_pairs(arr):
    symmetric_pairs = []
    seen_pairs = set()
    
    for pair in arr:
        reversed_pair = tuple(reversed(pair))
        
        if reversed_pair in seen_pairs:
            symmetric_pairs.append(pair)
            symmetric_pairs.append(reversed_pair)
        else:
            seen_pairs.add(pair)
    
    return symmetric_pairs

# Example input: array of pairs
pairs = [(1, 2), (3, 4), (2, 1), (5, 6), (6, 5)]

symmetric_pairs = find_symmetric_pairs(pairs)

print("Symmetric Pairs:")
for pair in symmetric_pairs:
    print(pair)
