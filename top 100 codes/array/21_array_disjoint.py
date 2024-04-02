def find_disjoint(set1, set2):
    disjoint_set = []
    
    for element in set1:
        if element not in set2:
            disjoint_set.append(element)
    
    for element in set2:
        if element not in set1 and element not in disjoint_set:
            disjoint_set.append(element)
    
    return disjoint_set

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
disjoint_elements = find_disjoint(set1, set2)
print("Disjoint elements:", disjoint_elements)
