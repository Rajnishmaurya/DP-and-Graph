class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = -1
        q = -1
        n = len(nums)
        i = 1
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        p = i - 1
        if p == 0 or p == n - 1:
            return False
        while i < n and nums[i] < nums[i - 1]:
            i += 1
        q = i - 1
        if q == n - 1:
            return False
        while i < n:
            if not (nums[i] > nums[i - 1]):
                return False
            i += 1
        return True