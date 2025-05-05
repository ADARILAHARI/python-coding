def generate_numbers(n):
    for i in range(n):
        yield i

# Test
for num in generate_numbers(5):
    print(num)
