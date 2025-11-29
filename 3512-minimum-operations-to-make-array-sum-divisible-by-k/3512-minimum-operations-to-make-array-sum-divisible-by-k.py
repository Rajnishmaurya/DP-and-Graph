class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sm = sum(nums)
        r = sm % k
        return r