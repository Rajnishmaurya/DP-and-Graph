class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=int(1e9)+7

        dp=[0]*26

        index=[ord(s[i])-ord('a') for i in range(len(s)-1,-1,-1)]

        for char in index:
            dp[char]=(1+sum(dp))%mod
        return sum(dp)%mod
    
        