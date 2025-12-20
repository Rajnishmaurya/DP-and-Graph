class Solution:
    def minDeletionSize(self, a: List[str]) -> int:
        return sum(any(map(gt,q,q[1:])) for q in zip(*a))