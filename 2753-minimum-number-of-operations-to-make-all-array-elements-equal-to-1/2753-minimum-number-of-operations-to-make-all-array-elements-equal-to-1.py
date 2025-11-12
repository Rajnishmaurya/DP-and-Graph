class Solution:
    def minOperations(self, nums: List[int]) -> int:

        min_steps, counter = float("inf"), Counter(nums)
        if 1 in counter: return len(nums) - counter[1]
        for i in range(len(nums)):
            cur_gcd = nums[i]
            for j in range(i + 1, len(nums)):
                cur_gcd = math.gcd(cur_gcd, nums[j])
                if cur_gcd == 1:
                    min_steps = min(min_steps, j - i)
                    break
        return min_steps + len(nums) - 1 if min_steps != float("inf") else -1