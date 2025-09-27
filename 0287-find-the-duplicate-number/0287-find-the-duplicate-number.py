class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp=defaultdict(int)
        ans=0
        for i in range(len(nums)):
            if  nums[i] in temp:
                ans=nums[i]
                break
            temp[nums[i]]+=1
        return ans