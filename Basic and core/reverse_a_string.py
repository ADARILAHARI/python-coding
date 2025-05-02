# Q1. Reverse a string (without [::-1])

def reverse(s):
    result = ''
    for char in s:
        result = char + result 
    return result

print(reverse("abbace"))

# Q2. Reverse a string (with [::-1])

def reverse_string(s):
    return s[::-1]

# Test
print(reverse_string("hello"))  # Output: 'olleh'
