class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.graph=defaultdict(list)
        for start,end,value in edges:
            self.graph[start].append((end,value))
        

    def addEdge(self, edge: List[int]) -> None:
        start,end,value=edge
        self.graph[start].append((end,value))

        

    def shortestPath(self, node1: int, node2: int) -> int:
        n=len(self.graph)

        heap=[]
        heap.append((0,node1))
        distance=[float('inf') for _ in range(self.n)]
        distance[node1]=0
        
        while heap:
            value,node=heapq.heappop(heap)
            if node==node2:
                return value
            for end,d in self.graph[node]:
                if value+d<distance[end]:
                    distance[end]=value+d
                    heapq.heappush(heap,(distance[end],end))
        return -1

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)