class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        seen=set(nums)
        ans=0

        for num in nums:
            x=num
            longest=0

            while x in seen:
                longest+=1
                x=x*x
            ans=max(ans,longest)
        
        return ans if ans>=2 else -1