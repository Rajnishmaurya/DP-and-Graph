class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.graph=defaultdict(list)
        for x,y,w in edges:
            self.graph[x].append((y,w))

    def addEdge(self, edge: List[int]) -> None:
        x,y,w=edge
        self.graph[x].append((y,w))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        n=len(self.graph)

        distance=[float('inf') for _ in range(self.n)]
        heap=[]
        heapq.heappush(heap,(0,node1))
        distance[node1]=0

        while heap:
            val,node=heapq.heappop(heap)
            if node==node2:
                return val
            for temp,val1 in self.graph[node]:
                if distance[temp]>val+val1:
                    distance[temp]=val+val1
                    heapq.heappush(heap,(distance[temp],temp))
        return -1


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)