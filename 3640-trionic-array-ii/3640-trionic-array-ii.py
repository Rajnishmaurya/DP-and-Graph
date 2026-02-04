class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float('inf')]*3 
        maxval = -float('inf')

        for (x, y) in pairwise(nums):
            dp[2] = max(dp[2], dp[1]) + y if y > x else -float('inf')
            dp[1] = max(dp[1], dp[0]) + y if y < x else -float('inf')
            dp[0] = max(dp[0], x) + y if y > x else -float('inf')
            maxval = max(maxval, dp[2])
        
        return maxval
        