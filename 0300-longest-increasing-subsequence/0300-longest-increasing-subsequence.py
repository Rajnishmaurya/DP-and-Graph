class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        lis=[nums[0]]
        length=1

        for i in range(1,n):
            if nums[i]>lis[-1]:
                length+=1
                lis.append(nums[i])
            else:
                index=bisect_left(lis,nums[i])
                lis[index]=nums[i]
        
        return length

        