from collections import Counter

def char_freq_file(filename):
    with open(filename, 'r') as f:
        return dict(Counter(f.read()))

# Test
# print(char_freq_file('sample.txt'))
