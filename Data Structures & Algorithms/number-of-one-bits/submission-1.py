class Solution:
    def hammingWeight(self, n: int) -> int:
        # result = 0
        # while n:
        #     result += n % 2
        #     n = n >> 1
        # return result
        # Karnighans algorithm
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
        