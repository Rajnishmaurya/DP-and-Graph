class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list=defaultdict(list)

        for i, (x,y) in enumerate(edges):
            adj_list[x].append((y,succProb[i]))
            adj_list[y].append((x,succProb[i]))
        
        heap=[(-1.0,start_node)]
        arr=[0.0]*n

        arr[start_node]=1.0

        while heap:
            current_prob,node=heapq.heappop(heap)
            current_prob=abs(current_prob)

            if node==end_node:
                return current_prob
            
            for neighbour,prob in adj_list[node]:
                new_prob=prob*current_prob
                if new_prob>arr[neighbour]:
                    arr[neighbour]=new_prob
                    heapq.heappush(heap,(-new_prob,neighbour))
        return 0.0

            

        