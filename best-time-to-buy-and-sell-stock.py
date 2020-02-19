# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for x in prices:
            min_price = min(x, min_price)
            max_profit = max(max_profit, x - min_price)
        return max_profit
