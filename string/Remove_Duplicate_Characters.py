def remove_duplicates(s):
    seen = set()
    result = ''
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Test
print(remove_duplicates("programming"))  # Output: 'progamin'
