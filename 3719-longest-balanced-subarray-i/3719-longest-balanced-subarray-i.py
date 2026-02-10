class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        output: int = 0
        n: int = len(nums)
        for i in range(n):
            odd: set[int] = set()
            even: set[int] = set()
            for j in range(i, n):
                if nums[j] & 1: odd.add(nums[j])
                else: even.add(nums[j])
                if len(odd) == len(even): output = max(output, j - i + 1)
        return output