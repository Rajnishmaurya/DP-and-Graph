class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses

        graph=defaultdict(list)

        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)  

        answer=[]

        while q:
            temp=q.popleft()
            answer.append(temp)
            for neighbor in graph[temp]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        if len(answer)==numCourses:
            return answer
        else:
            return []