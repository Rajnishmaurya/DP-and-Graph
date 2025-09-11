class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        heights=[0]*n
        count=0

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    heights[j]+=1
                else:
                    heights[j]=0
            
            for j in range(n):
                mini=heights[j]
                k=j
                while k>=0 and mini>0:
                    mini=min(mini,heights[k])
                    count+=mini
                    k-=1
        return count
        