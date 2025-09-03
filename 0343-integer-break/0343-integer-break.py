class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        if n==3:
            return 2
        
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        dp[3]=3

        for num in range(4,n+1):
            maxi=0
            for i in range(1,num//2+1):
                maxi=max(maxi,dp[i]*dp[num-i])
            dp[num]=maxi
        return dp[n]
