class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        for price in prices:
            profit = price - min_price
            if price < min_price:
                min_price = price
            if profit > best:
                best = profit
        return best