class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        buying = prices[0]
        for price in prices[1:]:
            if price > buying:
                max_profit = max(max_profit, price-buying)
            else:
                buying = price
        return max_profit
                