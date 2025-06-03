class Solution(object):
    def comb2(self, n):
        if n < 0:
            return 0
        return n * (n - 1) // 2

    def comb(self, n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        if k == 1:
            return n
        if k == 2:
            return n * (n - 1) // 2
        # Not needed for k > 2
        return 0

    def distributeCandies(self, n, limit):
        total = self.comb(n + 2, 2)

        if n >= limit + 1:
            total -= 3 * self.comb(n - (limit + 1) + 2, 2)

        if n >= 2 * (limit + 1):
            total += 3 * self.comb(n - 2 * (limit + 1) + 2, 2)

        if n >= 3 * (limit + 1):
            total -= self.comb(n - 3 * (limit + 1) + 2, 2)

        return total
