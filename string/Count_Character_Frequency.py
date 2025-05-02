#2. Count Character Frequency
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Test
print(char_frequency("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}
