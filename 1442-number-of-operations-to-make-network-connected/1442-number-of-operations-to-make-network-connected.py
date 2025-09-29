class Solution:
    def dfs(self,node,visited,adj):
        visited[node]=1
        for temp in adj[node]:
            if visited[temp]==0:
                self.dfs(temp,visited,adj)
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        temp=len(connections)
        if temp<n-1:
            return -1

        visited=[0]*n
        count=0
        adj=defaultdict(list)

        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
        
        for i in range(n):
            if visited[i]==0:
                count+=1
                self.dfs(i,visited,adj)
        return count-1
        