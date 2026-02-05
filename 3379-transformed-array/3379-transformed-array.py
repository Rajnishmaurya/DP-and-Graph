class Solution:
    def constructTransformedArray(self, a: List[int]) -> List[int]:
        return [a[(i+v)%len(a)] for i,v in enumerate(a)]