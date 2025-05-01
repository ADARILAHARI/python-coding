def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test
print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]
