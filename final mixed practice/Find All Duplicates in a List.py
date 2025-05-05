from collections import Counter

def find_duplicates(nums):
    freq = Counter(nums)
    return [num for num, count in freq.items() if count > 1]

print(find_duplicates([1, 2, 2, 3, 4, 4]))  # [2, 4]
