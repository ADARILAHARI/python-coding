#Rotate a List Left/Right
def rotate_left(lst, k):
    k %= len(lst)
    return lst[k:] + lst[:k]

def rotate_right(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

# Test
print(rotate_left([1, 2, 3, 4], 1))   # [2, 3, 4, 1]
print(rotate_right([1, 2, 3, 4], 1))  # [4, 1, 2, 3]
