import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        cost_edges = [[] for _ in range(n)]
        for u, v, w in edges:
            cost_edges[u].append((v, w))
            cost_edges[v].append((u, 2*w))
        
        INF = 10**18
        dist = [INF] * n

        dist[0] = 0
        pq = [(0, 0)]    # cost, node

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue
            
            for (v, w) in cost_edges[u]:
                if (cost + w) < dist[v]:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[n-1] if dist[n-1] < INF else -1