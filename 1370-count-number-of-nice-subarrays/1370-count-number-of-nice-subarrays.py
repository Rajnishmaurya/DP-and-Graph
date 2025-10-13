from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
            
        total=0
        count=0
        st=defaultdict(int)
        for num in nums:
            total+=num
            if total==k:
                count+=1
            if total-k in st:
                count+=st[total-k]
            st[total]+=1
        
        return count
        