class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        count=0
        ans=0

        while right<len(nums):
            if nums[right]==0:
                count+=1
            while count>1 and left<right:
                if nums[left]==0:
                    count-=1
                left+=1
            ans=max(ans,right-left)
            right+=1
        return ans
        