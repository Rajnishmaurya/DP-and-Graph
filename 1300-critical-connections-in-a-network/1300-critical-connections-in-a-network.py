class Solution:
    def dfs(self,node,parent,result,tin,low,timer,adj,visited):
        visited[node]=1

        tin[node]=timer
        low[node]=timer
        timer+=1
        for temp in adj[node]:
            if temp==parent:
                continue
            
            elif visited[temp]==0:
                self.dfs(temp,node,result,tin,low,timer,adj,visited)
                low[node]=min(low[node],low[temp])

                if low[temp]>tin[node]:
                    result.append([node,temp])
            else:
                low[node]=min(low[node],low[temp])



    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        result=[]
        tin=[0]*n
        low=[0]*n
        visited=[0]*n
        timer=1

        adj=defaultdict(list)

        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
        
        self.dfs(0,-1,result,tin,low,timer,adj,visited)
        return result