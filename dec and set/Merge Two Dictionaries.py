def merge_dicts(d1, d2):
    return {**d1, **d2}

# Test
print(merge_dicts({'a': 1}, {'b': 2}))  # Output: {'a': 1, 'b': 2}
