def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Test
print(safe_divide(10, 0))  # Output: Cannot divide by zero
