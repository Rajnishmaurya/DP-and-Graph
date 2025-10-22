class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q=deque()
        visited=set()
        q.append(x)
        steps=0

        while q:
            n=len(q)

            for _ in range(n):
                temp=q.popleft()
                if temp==y:
                    return steps
                visited.add(temp)

                if temp%11==0 and temp//11 not in visited:
                    q.append(temp//11)
                if temp%5==0 and temp//5 not in visited:
                    q.append(temp//5)
                if temp+1 not in visited:
                    q.append(temp+1)
                if temp-1 not in visited:
                    q.append(temp-1)
            steps+=1
        return -1
        