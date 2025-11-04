class Solution:
    def minOperations(self, n: int) -> int:
        step=0

        while n!=0:
            power=round(log2(abs(n)))
            if n>0:
                n-=2**power
            else:
                n+=2**power
            step+=1
        return step
        