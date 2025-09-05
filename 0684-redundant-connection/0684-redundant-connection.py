class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1

        adj_list=defaultdict(list)
        degree=[0]*n

        for x,y in edges:
            degree[x]+=1
            degree[y]+=1
            adj_list[x].append(y)
            adj_list[y].append(x)

        q=deque()

        for i,d in enumerate(degree):
            if d==1:
                q.append(i)
        
        removed=set()

        while q:
            node=q.popleft()
            removed.add(node)
            for neighbour in adj_list[node]:
                degree[neighbour]-=1
                if degree[neighbour]==1:
                    q.append(neighbour)
        for u,v in reversed(edges):
            if u not in removed and v not in removed:
                return [u,v]


        