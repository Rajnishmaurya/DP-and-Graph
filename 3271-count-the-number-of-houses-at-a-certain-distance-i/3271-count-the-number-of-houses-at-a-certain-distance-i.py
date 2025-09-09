class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        dp=[[200]*(n+1) for _ in range(n+1)]

        for i in range(1,n):
            dp[i][i+1]=1
            dp[i+1][i]=1
        dp[x][y]=1
        dp[y][x]=1

        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
        
        result=[0]*n

        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:
                    value=dp[i][j]
                    result[value-1]+=1
        return result


        