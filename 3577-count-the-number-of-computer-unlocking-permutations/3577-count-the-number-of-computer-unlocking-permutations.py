class Solution:
    def countPermutations(self, a: List[int]) -> int:
        return a[0]<min(a[1:]) and factorial(len(a)-1)%(10**9+7) or 0