class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        heap=[(0,start[0],start[1])]
        visited=set()
        ti,tj=target

        while heap:
            cost,i,j=heapq.heappop(heap)
            if (i,j) not in visited:
                visited.add((i,j))
            else:
                continue
            if (i,j)==(ti,tj):
                return cost
            heapq.heappush(heap,(cost+abs(ti-i)+abs(tj-j),ti,tj))

            for si,sj,di,dj,temp in specialRoads:
                road_cost = min(temp, abs(si - di) + abs(sj - dj))
                total_cost = cost + abs(i - si) + abs(j - sj) + road_cost
                heapq.heappush(heap,(total_cost,di,dj))


        