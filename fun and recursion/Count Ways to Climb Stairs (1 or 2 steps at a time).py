def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n-1) + count_ways(n-2)

# Test
print(count_ways(4))  # Output: 5
