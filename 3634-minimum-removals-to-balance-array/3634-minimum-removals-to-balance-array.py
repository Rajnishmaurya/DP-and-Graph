from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        l = 0
        max_len = 0
        
        for r in range(n):
            while nums[r] > k * nums[l]:
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return n - max_len