class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if prices is None or len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        
        min_price = prices[0] 
        max_profit = 0 
        
        for i in range(1, len(prices)):
            profit = prices[i] - min_price           
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])
        
        return max_profit