class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        parent = list(range(n))
        know = [False] * n
        know[0] = know[firstPerson] = True

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        i = 0
        while i < len(meetings):
            t = meetings[i][2]
            temp = []

            j = i
            while j < len(meetings) and meetings[j][2] == t:
                union(meetings[j][0], meetings[j][1])
                temp += meetings[j][:2]
                j += 1

            for x in temp:
                if know[x]:
                    know[find(x)] = True

            for x in temp:
                know[x] |= know[find(x)]

            for x in temp:
                parent[x] = x

            i = j

        return [i for i in range(n) if know[i]]