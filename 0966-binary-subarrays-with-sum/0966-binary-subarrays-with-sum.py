from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total=0
        count=0

        st=defaultdict(int)

        for num in nums:
            total+=num
            if total==goal:
                count+=1
            
            if total-goal in st:
                count+=st[total-goal]
            st[total]+=1
        
        return count
        