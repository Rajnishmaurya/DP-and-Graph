class Solution:
    def  bfs(self,graph,n):
        q=deque()
        q.append(0)
        visited=set()
        ans=0

        while q:
            for _ in range(len(q)):
                temp=q.popleft()
                if temp==n-1:
                    return ans
                for v in graph[temp]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            ans+=1
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]

        for i in range(n-1):
            graph[i].append(i+1)
        ans=[]
        for u,v in queries:
            graph[u].append(v)
            ans.append(self.bfs(graph,n))
        return ans
        