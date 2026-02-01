class Solution:
    def minimumCost(self, a: List[int]) -> int:
        return a[0]+sum(sorted(a[1:])[:2])