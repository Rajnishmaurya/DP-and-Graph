class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        if total % 3 == 0:
            return total
        
        one_srt = sorted([x for x in nums if x % 3 == 1])
        two_srt = sorted([x for x in nums if x % 3 == 2])
        
        result = 0
        
        if total % 3 == 1:
            del_one = 0
            if one_srt:
                del_one = total - one_srt[0]
            
            del_two = 0
            if len(two_srt) >= 2:
                del_two = total - two_srt[0] - two_srt[1]
            
            result = max(del_one, del_two)
        else:  
            del_two = 0
            if two_srt:
                del_two = total - two_srt[0]
            
            del_one = 0
            if len(one_srt) >= 2:
                del_one = total - one_srt[0] - one_srt[1]
            
            result = max(del_one, del_two)
        
        return result