def most_frequent(lst):
    freq = count_frequency(lst)
    return max(freq, key=freq.get)

# Test
print(most_frequent([1, 2, 2, 3, 1, 1]))  # Output: 1
