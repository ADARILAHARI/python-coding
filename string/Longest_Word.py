def longest_word(s):
    words = s.split()
    return max(words, key=len)

# Test
print(longest_word("I love Python programming"))  # Output: 'programming'
