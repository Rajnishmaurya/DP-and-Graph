from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)

        for x,y,dis in roads:
            graph[x].append((y,dis))
            graph[y].append((x,dis))
        
        answer=float('inf')
        visited=set()
        q=deque()
        q.append(1)

        while q:
            temp=q.popleft()

            for neighbour , dist in graph[temp]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)
                answer=min(answer,dist)
        return answer


        