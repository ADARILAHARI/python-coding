import math

def gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return gcd, lcm

# Test
print(gcd_lcm(12, 18))  # (6, 36)
