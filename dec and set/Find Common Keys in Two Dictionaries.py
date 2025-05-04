def common_keys(d1, d2):
    return list(d1.keys() & d2.keys())

# Test
print(common_keys({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # Output: ['b']
