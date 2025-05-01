# Q1. Reverse a string (without [::-1])

def reverse(s):
    result = ''
    for char in s:
        result = char + result 
    return result

print(reverse("abbace"))