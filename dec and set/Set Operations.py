def set_operations(a, b):
    a, b = set(a), set(b)
    return {
        'union': a | b,
        'intersection': a & b,
        'difference': a - b
    }

# Test
print(set_operations([1, 2, 3], [2, 3, 4]))
# Output: {'union': {1, 2, 3, 4}, 'intersection': {2, 3}, 'difference': {1}}
