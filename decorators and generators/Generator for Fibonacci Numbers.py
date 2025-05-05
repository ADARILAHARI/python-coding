def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Test
print(list(fibonacci(10)))  # Output: [0, 1, 1, 2, 3, 5, 8]
