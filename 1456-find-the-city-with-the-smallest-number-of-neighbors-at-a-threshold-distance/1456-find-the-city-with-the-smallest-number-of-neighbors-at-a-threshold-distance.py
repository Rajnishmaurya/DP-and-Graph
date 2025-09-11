class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix=[[10001]*n for _ in range(n)]

        for i in range(n):
            matrix[i][i]=0
        
        for u,v,w in edges:
            matrix[u][v]=w
            matrix[v][u]=w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        count=n
        result=-1
        for i in range(n):
            total=sum(1 for j in range(n) if matrix[i][j]<=distanceThreshold)
            if total<=count:
                count=total
                result=i

        return result

        