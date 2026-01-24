class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return nums.sort() or max(nums[l] + nums[~l] for l in range(len(nums)>>1))