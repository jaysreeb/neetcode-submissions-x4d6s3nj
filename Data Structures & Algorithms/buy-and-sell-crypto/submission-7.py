class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minPrice = float('inf')
        for price in prices:
            profit = price - minPrice
            maxPrice = max(maxPrice, profit)
            minPrice = min(minPrice, price)
        return maxPrice
