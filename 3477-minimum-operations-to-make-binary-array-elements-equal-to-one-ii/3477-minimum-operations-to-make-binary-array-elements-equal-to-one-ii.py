class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result=0
        count=0
        n=len(nums)
        for i,num in enumerate(nums):
            if num==0:
                count+=1
            else:
                if count>0:
                    count=0
                    result+=2
                    
        if count:
            result+=1
        return result

        