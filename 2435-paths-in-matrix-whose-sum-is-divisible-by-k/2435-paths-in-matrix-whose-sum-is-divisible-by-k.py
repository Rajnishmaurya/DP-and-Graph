class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n,MOD = len(grid), len(grid[0]), int(1e9+7)
        dp  = [[[0]*k for _ in range(n+1)] for __ in range(2)]
        dp[0][-1][0] = 1
        for i in range(m):
            row = i%2
            for j in range(n):
                for r in range(k):
                    r_new = (r + grid[i][j]) %k
                    dp[row][j][r_new] = (dp[row-1][j][r] + dp[row][j-1][r]) %MOD
            dp[0][-1][0] = 0
        return  dp[row][n-1][0]
        