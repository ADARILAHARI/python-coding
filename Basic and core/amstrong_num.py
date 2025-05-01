def is_armstrong(n):
    digits = [int(x) for x in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

# Test
print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
