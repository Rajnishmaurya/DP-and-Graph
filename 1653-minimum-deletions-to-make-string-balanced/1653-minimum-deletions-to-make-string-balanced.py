class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count,result=0,0

        for c in s:
            if c=='b':
                count+=1
            elif count:
                result+=1
                count-=1
        return result