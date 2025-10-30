class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi=0
        mini=0
        ans=0
        for num in nums:
            maxi=max(maxi+num,0)
            mini=min(mini+num,0)
            ans=max(-mini,maxi,ans)
        return ans
        