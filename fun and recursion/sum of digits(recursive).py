def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# Test
print(sum_of_digits(1234))  # Output: 10
