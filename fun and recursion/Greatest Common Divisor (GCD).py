def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Test
print(gcd(48, 18))  # Output: 6
