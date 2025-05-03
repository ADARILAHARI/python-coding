def list_intersection(a, b):
    return list(set(a) & set(b))

def list_union(a, b):
    return list(set(a) | set(b))

# Test
print(list_intersection([1, 2, 3], [2, 3, 4]))  # [2, 3]
print(list_union([1, 2, 3], [2, 3, 4]))        # [1, 2, 3, 4]
