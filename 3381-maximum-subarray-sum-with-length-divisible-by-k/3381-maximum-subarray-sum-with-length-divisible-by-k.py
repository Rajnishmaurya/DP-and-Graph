class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        least_pre = [inf] * k
        least_pre[-1] = 0
        pre_sum = 0
        max_sum = -inf
        for i, num in enumerate(nums):
            pre_sum += num
            mod = i % k
            old_pre = least_pre[mod]
            sub_sum = pre_sum - old_pre
            if max_sum < sub_sum:
                max_sum = sub_sum
            if old_pre > pre_sum:
                least_pre[mod] = pre_sum
        return max_sum