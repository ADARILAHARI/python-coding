 #Q2. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Test
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
