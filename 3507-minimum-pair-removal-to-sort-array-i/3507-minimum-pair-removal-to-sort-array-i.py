class Solution:
    def minimumPairRemoval(self, nums):
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        operations = 0

        while not is_sorted(nums):
            min_sum = nums[0] + nums[1]
            idx = 0

            # Find leftmost adjacent pair with minimum sum
            for i in range(1, len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    idx = i

            # Merge the pair
            nums[idx] = min_sum
            nums.pop(idx + 1)
            operations += 1

        return operations