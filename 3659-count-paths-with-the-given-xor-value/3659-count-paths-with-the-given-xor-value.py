class Solution:
    def solve(self,grid,dp,i,j,curr,m,n,mod,k):
        if i>=m or j>=n:
            return 0
        
        curr^=grid[i][j]

        if i==m-1 and j==n-1:
            return 1 if curr==k else 0
        
        if dp[i][j][curr]!=-1:
            return dp[i][j][curr]
        
        right=self.solve(grid,dp,i,j+1,curr,m,n,mod,k)
        down=self.solve(grid,dp,i+1,j,curr,m,n,mod,k)

        dp[i][j][curr]=(right+down)%mod

        return dp[i][j][curr]


    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod=int(1e9)+7
        m,n=len(grid),len(grid[0])
        dp=[[[-1 for _ in range(20)] for _ in range(n)] for _ in range(m)]
        return self.solve(grid,dp,0,0,0,m,n,mod,k)
        