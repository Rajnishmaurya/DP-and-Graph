class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0]*n

        for u,v in edges:
            indegree[v]+=1
        
        champions=[i for i in range(n) if indegree[i]==0]

        if len(champions)==1:
            return champions[0]
        else:
            return -1
        