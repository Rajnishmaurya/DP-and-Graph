class Solution:
    def minimumBoxes(self, a: List[int], c: List[int]) -> int:
        return sum(map(lt,accumulate(sorted(c)[::-1]),repeat(sum(a))))+1     