def subsets(lst):
    result = []
    def backtrack(index, path):
        if index == len(lst):
            result.append(path)
            return
        backtrack(index + 1, path)
        backtrack(index + 1, path + [lst[index]])
    backtrack(0, [])
    return result

# Test
print(subsets([1, 2]))  # Output: [[], [2], [1], [1, 2]]

