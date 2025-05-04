def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test
print([fibonacci(i) for i in range(7)])  # Output: [0, 1, 1, 2, 3, 5, 8]
