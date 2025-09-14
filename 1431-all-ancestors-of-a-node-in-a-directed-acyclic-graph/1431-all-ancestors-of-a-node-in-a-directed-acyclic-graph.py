class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        reverse_graph=defaultdict(list)
        indegree=[0]*n

        for u,v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)
            indegree[v]+=1
        
        q=deque()

        for i in range(n):
            if indegree[i]==0:
                q.append(i)
            
        topo_order=[]

        while q:
            temp=q.popleft()
            topo_order.append(temp)
            for node  in graph[temp]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        
        ancestors=[set() for i in range(n)]

        for node in topo_order:
            for temp in reverse_graph[node]:
                ancestors[node].add(temp)
                ancestors[node].update(ancestors[temp])
        
        result=[sorted(list(val)) for val in ancestors]
        return result
        
        