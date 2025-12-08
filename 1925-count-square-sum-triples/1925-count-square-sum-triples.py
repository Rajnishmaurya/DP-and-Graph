class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1,n+1):
            a2 = a*a
            for b in range(1,n+1):
                s = a2+b*b
                c = math.isqrt(s)
                if c*c == s and c <= n :
                    count +=1
        return count