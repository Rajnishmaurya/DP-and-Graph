class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        for c in cuboids:
            c.sort()
        
        cuboids.sort()

        n=len(cuboids)

        dp=[c[2] for c in cuboids]


        for i in range(n):
            for j in range(i):
                if cuboids[i][0]>=cuboids[j][0] and cuboids[i][1]>=cuboids[j][1] and cuboids[i][2]>=cuboids[j][2]:
                    dp[i]=max(dp[i],dp[j]+cuboids[i][2])
        return max(dp)
        