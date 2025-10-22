class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list=defaultdict(list)
        n=len(roads)
        indegree=[0]*(n+1)

        people=[1]*(n+1)

        for x,y in roads:
            adj_list[x].append(y)
            adj_list[y].append(x)
            indegree[x]+=1
            indegree[y]+=1
        
        q=deque()

        for i in range(1,n+1):
            if indegree[i]==1:
                q.append(i)
            
        ans=0

        while q:
            temp=q.popleft()
            ans+=ceil(people[temp]/seats)

            for node in adj_list[temp]:
                indegree[node]-=1
                people[node]+=people[temp]
                if indegree[node]==1 and node!=0:
                    q.append(node)
        return ans


        
        