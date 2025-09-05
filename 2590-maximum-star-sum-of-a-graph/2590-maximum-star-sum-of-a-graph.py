class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

        n=len(vals)

        adj_list=defaultdict(list)

        for x,y in edges:
            adj_list[x].append(vals[y])
            adj_list[y].append(vals[x])
        
        answer=float("-inf")

        for i in range(n):
            best_neighbour=nlargest(k,[v for v in adj_list[i] if v>0])
            temp=vals[i]+sum(best_neighbour)
            answer=max(answer,temp)

        return answer