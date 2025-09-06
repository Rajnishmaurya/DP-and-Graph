class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n=len(s)
        mod=10**9+7
        @lru_cache(None)
        def solve(i,val):
            if i==n:
                return 1
            if s[i]=='D':
                if val==0:
                    return 0
                else:
                    return solve(i,val-1)+solve(i+1,val-1)
            if  s[i]=='I':
                if val==n-i:
                    return 0
                return solve(i,val+1)+solve(i+1,val)
        
        return sum([solve(0,j) for j in range(n+1)])%mod

        