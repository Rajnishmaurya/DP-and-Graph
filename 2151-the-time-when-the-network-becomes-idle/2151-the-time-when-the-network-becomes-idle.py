class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph=defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        q=deque()
        q.append((0,0)) # node, distance
        distance={}
        visited=set()
        visited.add(0)
        while q:
            node,length=q.popleft()
            distance[node]=2*length

            for neighbour in graph[node]:
                if neighbour not in visited:
                    q.append((neighbour,length+1))
                    visited.add(neighbour)
        
        answer=float("-inf")
        for i in range(len(patience)):
            if patience[i]<distance[i]:
                rem=distance[i]%patience[i]
                temp=distance[i]-(rem) if rem>0 else distance[i]-patience[i]
                answer=max(answer,distance[i]+temp)
            else:
                answer=max(answer,distance[i])
        return answer+1

        