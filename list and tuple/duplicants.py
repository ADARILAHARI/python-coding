#Remove Duplicates from a List

def remove_duplicates(lst):
    return list(set(lst))

# Test
print(remove_duplicates([1, 2, 2, 3, 1]))  # Output: [1, 2, 3]
