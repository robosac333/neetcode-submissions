class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        mini = prices[0]
        profit = 0
        for candidate in prices:
            mini = min(mini, candidate)
            profit = max(profit, candidate-mini)
        return profit
