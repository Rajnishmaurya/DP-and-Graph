class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        dp=[0]*n

        maxi=values[0]
        answer=0

        for i in range(1,n):
            dp[i]=maxi+values[i]-i
            maxi=max(maxi,values[i]+i)
            answer=max(answer,dp[i])
        return answer

        