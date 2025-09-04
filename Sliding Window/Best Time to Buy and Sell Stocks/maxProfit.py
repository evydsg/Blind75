class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(len(prices)):

            while prices[left] > prices[right]:
                left += 1
            
            max_profit = max(prices[right] - prices[left], max_profit)
        
        return max_profit