def strstr(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Test
print(strstr("hello world", "world"))  # Output: 6

