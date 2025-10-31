class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans=0
        prefix=0
        for i,num in enumerate(nums):
            prefix+=num
            ans=max(ans,(prefix+i)//(i+1))
        return ans