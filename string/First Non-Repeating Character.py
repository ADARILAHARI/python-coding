def first_non_repeating(s):
    from collections import OrderedDict
    freq = OrderedDict()
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        if count == 1:
            return char
    return None

# Test
print(first_non_repeating("aabbcddeff"))  # Output: 'c'
