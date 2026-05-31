class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_profit = 9999999, 0
        window = {}
        if len(prices)<1:
            return 0

        for candidate in prices:
            min_val = min(min_val, candidate)
            max_profit = max(max_profit, candidate - min_val)
        return max_profit