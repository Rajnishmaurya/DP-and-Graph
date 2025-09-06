class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        while sum(satisfaction)<0:
            satisfaction.pop()
        
        n=len(satisfaction)
        total=0
        for i in range(n):
            total+=(n-i)*satisfaction[i]
        return total
        
