class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for day in prices:
            profit = day - lowest_price
            if profit > max_profit:
                max_profit = profit
            if day < lowest_price:
                lowest_price = day
        return max_profit