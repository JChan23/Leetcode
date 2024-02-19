class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initialize 2D array
        dp = [[0]*(n) for _ in range(m)]
        for i in range(n):
            dp[m-1][i] = 1
        for i in range(m):
            dp[i][n-1] = 1
    
        #process
        i = m-2
        while i >= 0:
            j = n - 2
            while j >= 0:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
                j = j - 1
            i = i - 1
        return dp[0][0]
