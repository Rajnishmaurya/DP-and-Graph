class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans=0
        prev=0
        n=len(colors)
        for i in range(1,n):
            if colors[prev]!=colors[i]:
                prev=i
            else:
                ans+=min(neededTime[prev],neededTime[i])
                if neededTime[prev]<neededTime[i]:
                    prev=i
        return ans
        