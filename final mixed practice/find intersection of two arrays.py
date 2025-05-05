def intersect(a, b):
    return list(set(a) & set(b))

print(intersect([1,2,3], [2,3,4]))  # [2, 3]
