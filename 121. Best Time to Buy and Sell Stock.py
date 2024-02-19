class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointer approach - indexes
        left = 0
        right = 1
        MaxProfit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                MaxProfit = max(MaxProfit, profit)
            else:
                left = right
            right = right + 1
        return MaxProfit
