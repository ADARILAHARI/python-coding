from collections import defaultdict

def group_by_frequency(lst):
    freq = defaultdict(list)
    for item in lst:
        freq[lst.count(item)].append(item)
    return dict(freq)

# Test
print(group_by_frequency([1, 2, 2, 3, 3, 3]))
# Output: {1: [1], 2: [2, 2], 3: [3, 3, 3]}
