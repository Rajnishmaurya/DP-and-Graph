class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        visited=set()
        visited.add(1)

        heap=[]
        heapq.heappush(heap,1)

        for i in range(n):
            temp=heapq.heappop(heap)

            for num in primes:
                current=temp*num
                if current not in visited:
                    visited.add(current)
                    heapq.heappush(heap,current)
        return temp