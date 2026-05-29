class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        res = 999999
        profit = 0
        for index, candidate in enumerate(prices):
            if candidate < res:
                res = candidate
            profit = max(profit, candidate-res)

        return profit
