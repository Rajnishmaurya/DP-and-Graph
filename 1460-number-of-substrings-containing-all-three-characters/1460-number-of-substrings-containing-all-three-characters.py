class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen=[-1]*3
        count=0
        for i in range(len(s)):
            lastseen[ord(s[i])-ord()]        