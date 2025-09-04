class Solution:
    def numOfWays(self, n: int) -> int:
        color3=6
        color2=6
        mod=int(1e9)+7
        for i in range(n-1):
            temp=color3
            color3=2*color2+2*color3
            color2=2*temp+3*color2

        return (color2+color3)%mod
        