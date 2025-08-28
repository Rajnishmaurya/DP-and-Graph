class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)

        arr=[0]*n
        arr[0]=1
        q=deque()

        for i in rooms[0]:
            q.append(i)
        
        while q:
            temp=q.pop()

            if arr[temp]==0:
                arr[temp]=1
                for i in rooms[temp]:
                    q.append(i)
        for i in range(n):
            if arr[i]==0:
                return False
        return True


        