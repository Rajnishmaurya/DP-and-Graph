class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total=0
        n=len(arr)

        for i in range(n):
            for j in range(i,n):
                total+=min(arr[i:j+1])
        return total

        