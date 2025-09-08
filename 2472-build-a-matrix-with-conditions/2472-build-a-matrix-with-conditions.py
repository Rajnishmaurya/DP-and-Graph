class Solution:
    def topo(self,edges,k):
        graph=defaultdict(list)
        indegree=[0]*k

        for x,y in edges:
            graph[x-1].append(y-1)
            indegree[y-1]+=1
        
        q=deque()
        for i in range(k):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            temp=q.popleft()
            ans.append(temp+1)

            for node in graph[temp]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        return ans

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row=self.topo(rowConditions,k)
        col=self.topo(colConditions,k)
        if len(row)<k or len(col)<k:
            return []
        row={x:i for i,x in enumerate(row)}
        col={x:i for i,x in enumerate(col)}

        ans=[[0]*k for _ in range(k)]

        for x in range(1,k+1):
            ans[row[x]][col[x]]=x
        return ans


        