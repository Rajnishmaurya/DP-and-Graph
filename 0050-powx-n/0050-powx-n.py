class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        temp=n
        if temp<0:
            temp=abs(n)
        
        while temp:
            if temp%2:
                temp-=1
                ans=ans*x
            else:
                temp=temp//2
                x=x*x
        if n<0:
            return 1/ans
        else:
            return ans
        