class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            maxi=1e-9
            ans_sum=1e-9
            length=0
            for j in range(i,min(i+k,n)):
                length+=1
                maxi=max(maxi,arr[j])
                sum=length*maxi+dp[j+1]
                ans_sum=max(ans_sum,sum)
            dp[i]=ans_sum
        return dp[0]
        