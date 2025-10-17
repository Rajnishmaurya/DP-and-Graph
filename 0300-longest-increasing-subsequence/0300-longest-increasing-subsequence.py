import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[]
        lis.append(nums[0])
        for i in range(1,len(nums)):
            if lis[-1]<nums[i]:
                lis.append(nums[i])
            else:
                index=bisect.bisect_left(lis,nums[i])
                lis[index]=nums[i]
        return len(lis)
        