def lexicographic_permutations(sorted_string):
    n = len(sorted_string)
    current_permutation = list(sorted_string)
    
    while True:
        print(''.join(current_permutation))
        
        # Find the largest index i such that current_permutation[i] < current_permutation[i+1]
        i = n - 2
        while i >= 0 and current_permutation[i] >= current_permutation[i + 1]:
            i -= 1
        
        # If there is no such i, we have generated all permutations
        if i == -1:
            break
        
        # Find the largest index j such that current_permutation[j] > current_permutation[i]
        j = n - 1
        while current_permutation[j] <= current_permutation[i]:
            j -= 1
        
        # Swap current_permutation[i] and current_permutation[j]
        current_permutation[i], current_permutation[j] = current_permutation[j], current_permutation[i]
        
        # Reverse the substring after i
        current_permutation[i + 1:] = reversed(current_permutation[i + 1:])

# Input string from the user
string = input("Enter a string: ")

# Sort the string for lexicographic order
sorted_string = ''.join(sorted(string))

# Call the function to print lexicographic permutations
lexicographic_permutations(sorted_string)
