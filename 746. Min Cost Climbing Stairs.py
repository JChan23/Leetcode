class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf') for i in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = min(cost[i]+dp[i-2], cost[i]+dp[i-1])
        return min(dp[len(cost)-1], dp[len(cost)-2])
