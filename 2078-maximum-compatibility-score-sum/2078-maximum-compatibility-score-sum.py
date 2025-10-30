from itertools import permutations
from typing import List
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m,n=len(students),len(students[0])

        score=[[0]*m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                score[i][j]=sum(students[i][k]==mentors[j][k] for k in range(n))
        
        ans=0

        for perm in permutations(range(m)):
            temp=sum(score[i][perm[i]] for i in range(m))
            ans=max(ans,temp)
        return ans


        