class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count=0
        result=0

        for c in s:
            if c=='0':
                if count:
                    result+=1
                    count-=1
            else:
                count+=1
        return result
        