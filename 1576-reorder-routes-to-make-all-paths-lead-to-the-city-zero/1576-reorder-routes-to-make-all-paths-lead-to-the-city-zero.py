class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list=defaultdict(list)

        for x,y in connections:
            adj_list[x].append((y,1))
            adj_list[y].append((x,0))

        q=deque()
        q.append(0)
        visited=[False]*n
        visited[0]=True
        answer=0
        while q:
            temp=q.popleft()

            for neighbour,score in adj_list[temp]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    answer+=score
                    q.append(neighbour)
        return answer
                

        