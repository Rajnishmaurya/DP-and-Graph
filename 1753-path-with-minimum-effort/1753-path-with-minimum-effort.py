class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])

        heap=[]
        heapq.heappush(heap,(0,0,0))

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        distance=[[1e9 for _ in range(n)] for _ in range(m)]
        distance[0][0]=0
        while heap:
            diff,r,c=heapq.heappop(heap)

            if r==m-1 and c==n-1:
                return diff
            
            for x,y in directions:
                nr=x+r
                nc=y+c

                if nr in range(m) and nc in range(n):
                    temp=max(diff,abs(heights[nr][nc]-heights[r][c]))
                    if temp<distance[nr][nc]:
                        distance[nr][nc]=temp
                        heapq.heappush(heap,(temp,nr,nc))
        return 0
            
