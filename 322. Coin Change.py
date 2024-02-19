class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf') for i in range(amount + 1)] 
        dp[0] = 0 

        for i in range(len(dp)):
            for j in coins: 
                if i-j >= 0: 
                    dp[i] = min(dp[i], dp[i-j] + 1)

        if dp[-1] == float('inf'):
            return -1
        else:
            return int(dp[-1])
