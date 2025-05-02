def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Test
print(reverse_words("I love Python"))  # Output: 'Python love I'
