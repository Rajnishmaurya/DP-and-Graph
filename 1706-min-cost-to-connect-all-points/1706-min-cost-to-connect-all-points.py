class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        heap=[]
        answer=0
        visited.add(0)

        for i in range(1,n):
            d=abs(points[0][0]-points[i][0])+abs(points[0][1]-points[i][1])
            heapq.heappush(heap,(d,i))

        while heap:
            d,index=heapq.heappop(heap)
            if index in visited:
                continue
            visited.add(index)
            answer+=d

            for i in range(n):
                d=abs(points[index][0]-points[i][0])+abs(points[index][1]-points[i][1])
                heapq.heappush(heap,(d,i))
        
        return answer

        
