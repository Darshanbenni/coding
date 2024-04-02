def count_common_subsequences(string1, string2):
    def backtrack(index1, index2):
        if index1 == len(string1) or index2 == len(string2):
            return 1
        
        count = backtrack(index1 + 1, index2) + backtrack(index1, index2 + 1)
        if string1[index1] == string2[index2]:
            count += backtrack(index1 + 1, index2 + 1)
        
        return count
    
    return backtrack(0, 0)

# Input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function to count common subsequences
result = count_common_subsequences(string1, string2)

print(f"The number of common subsequences is: {result}")
