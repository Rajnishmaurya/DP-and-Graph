from collections import defaultdict
from typing import List
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj=defaultdict(list)

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        restricted=set(restricted)
        q=deque()
        q.append(0)
        count=0

        visited=set([0])
        if 0 in restricted:
            return 0

        while q:
            node=q.popleft()
            count+=1
            for temp in adj[node]:
                if temp not in restricted and temp not in visited:
                    q.append(temp)
                    visited.add(temp)
        return count
        