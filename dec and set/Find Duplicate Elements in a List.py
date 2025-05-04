def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

# Test
print(find_duplicates([1, 2, 2, 3, 3, 4]))  # Output: [2, 3]
