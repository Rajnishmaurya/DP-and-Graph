class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count=0

        while '01' in s:
            count+=1
            s=s.replace('01','10')
        return count
        
        