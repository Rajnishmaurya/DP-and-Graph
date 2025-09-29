class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)

        for x,y,price in flights:
            adj[x].append((y,price))
        
        distance=[1e9]*n

        q=deque()
        q.append((0,src,0))

        while q:
            step,source,dist=q.popleft()
            if step>k:
                continue
            
            for node,price in adj[source]:
                temp=price+dist
                if temp<distance[node]:
                    distance[node]=temp
                    q.append((step+1,node,temp))
        if distance[dst]!=1e9:
            return distance[dst]
        else:
            return -1
