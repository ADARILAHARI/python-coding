'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Input: Accept either comma-separated values or list
try:
    nums_input = input("Enter numbers (e.g., 2,7,11,15 or [2,7,11,15]): ")
    if '[' in nums_input:
        nums = eval(nums_input)
    else:
        nums = [int(x.strip()) for x in nums_input.split(',')]
except Exception as e:
    print("Invalid input format.")
    exit()

target = int(input("Enter target sum: "))

sol = Solution()
result = sol.twoSum(nums, target)

if result:
    print("Indices of elements that sum to target:", result)
else:
    print("No two numbers add up to the target.")

