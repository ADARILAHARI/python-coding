def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Test
print(count_frequency([1, 2, 2, 3, 1, 1]))  # Output: {1: 3, 2: 2, 3: 1}
