class Solution:
    def countTrapezoids(self, a: List[List[int]]) -> int:
        b = [comb(v,2) for v in Counter(y for _,y in a).values()]
        return sum(map(mul,b[1:],accumulate(b)))%(10**9+7)