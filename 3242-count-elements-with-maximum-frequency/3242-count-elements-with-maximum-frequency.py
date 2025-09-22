class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=[0]*101
        maxi=0
        for num in nums:
            count[num]+=1
            maxi=max(maxi,count[num])
        
        answer=0

        for i in range(1,101):
            if maxi==count[i]:
                answer+=count[i]
        return answer

        