class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n=len(values)

        dp={}

        def solve(i,j):
            if j-i<2:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            mini=float('inf')

            for k in range(i+1,j):
                score=values[i]*values[j]*values[k]+solve(i,k)+solve(k,j)

                mini=min(mini,score)
            dp[(i,j)]=mini
            return mini
        return solve(0,n-1)

        