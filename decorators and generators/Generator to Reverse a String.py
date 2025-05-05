def reverse_string(s):
    for i in range(len(s)-1, -1, -1):
        yield s[i]

print(''.join(reverse_string("hello")))  # Output: olleh
