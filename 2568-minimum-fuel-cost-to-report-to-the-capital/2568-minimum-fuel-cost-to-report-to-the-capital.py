class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list=defaultdict(list)
        n=len(roads)+1
        degree=[0]*n
        people=[1]*(n+1)

        for x,y  in roads:
            adj_list[x].append(y)
            adj_list[y].append(x)
            degree[x]+=1
            degree[y]+=1
        
        q=deque()
        for i in range(1,n):
            if degree[i]==1:
                q.append(i)
            
        answer=0

        while q:
            temp=q.popleft()
            answer+=ceil(people[temp]/seats)
            for neighbour in adj_list[temp]:
                degree[neighbour]-=1
                people[neighbour]+=people[temp]
                if degree[neighbour]==1 and neighbour!=0:
                    q.append(neighbour)
        return answer



        