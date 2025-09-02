class Solution:
    def twoEggDrop(self, n: int) -> int:
        step=0
        total=0
        while total<n:
            step+=1
            total+=step
        return step
        