class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        lastseen=[-1]*3
        for i in range(len(s)):
            lastseen[ord(s[i])-ord('a')]=i
            if lastseen[0]!=-1 and lastseen[1]!=-1 and lastseen[2]!=-1:
                count+=1+min(lastseen)
        return count