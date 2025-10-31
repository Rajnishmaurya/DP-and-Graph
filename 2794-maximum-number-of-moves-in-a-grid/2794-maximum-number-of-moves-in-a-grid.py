class Solution:
    # def solve(self,i,grid,m,n):
    #     q=deque()
    #     q.append((i,0,0))

    #     ans=0
    #     while q:
    #         x,y,step=q.popleft()
    #         ans=max(ans,step)
    #         if x in range(m) and y in range(n):
    #             if x+1<m and y+1<n and grid[x+1][y+1]>grid[x][y]:
    #                 q.append((x+1,y+1,step+1))
    #             if y+1<n and grid[x][y+1]>grid[x][y]:
    #                 q.append((x,y+1,step+1))
    #             if x-1>=0 and y+1<n and grid[x-1][y+1]>grid[x][y]:
    #                 q.append((x-1,y+1,step+1))
        # return ans
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        # ans=0

        # for i in range(m):
        #     ans=max(ans,self.solve(i,grid,m,n))
        # return ans
        
        dp=[[0]*n for _ in range(m)]

        for j in range(n-2,-1,-1):
            for i in range(m):
                for dx in (-1,0,1):
                    nr=i+dx
                    ny=j+1
                    if nr in range(m) and grid[nr][ny]>grid[i][j]:
                        dp[i][j]=max(dp[i][j],1+dp[nr][ny])
        
        return max(dp[i][0] for i in range(m))
        