class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m=len(s1)
        n=len(s2)
        total=0
        for i in range(m):
            total+=ord(s1[i])
        
        for j in range(n):
            total+=ord(s2[j])

        lcs=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    lcs[i][j]=lcs[i-1][j-1]+ord(s1[i-1])
                else:
                    lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
        return total-2*lcs[m][n]

        