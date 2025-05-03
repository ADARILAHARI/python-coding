def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# Test
print(second_largest([10, 20, 10, 40, 30]))  # Output: 30
