def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Test
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
