def is_subset(a, b):
    return set(a).issubset(set(b))

# Test
print(is_subset([1, 2], [1, 2, 3]))  # True
