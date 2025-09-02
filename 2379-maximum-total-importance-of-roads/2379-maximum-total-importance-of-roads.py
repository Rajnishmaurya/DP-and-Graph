class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree=[0]*n

        for x,y in roads:
            degree[x]+=1
            degree[y]+=1
        
        degree.sort()
        answer=0
        for i in range(n):
            answer+=(i+1)*degree[i]
        return answer
        