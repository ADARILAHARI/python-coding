from itertools import permutations

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = set()
        
        for comb in permutations(digits, 3):
            if comb[0] == 0:  # Skip numbers with leading zero
                continue
            
            number = comb[0] * 100 + comb[1] * 10 + comb[2]
            if number % 2 == 0:  # Check if the number is even
                result.add(number)
        
        return sorted(result)