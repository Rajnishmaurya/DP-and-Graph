from collections import defaultdict
class Solution:
    def maxProduct(self, s: str) -> int:
        if len(s)==2:
            return 1
        
        n=len(s)
        d=defaultdict(int)
        
        for mask in range(1,1<<n):
            subse=[s[i] for i in range(n) if mask&(1<<i)]

            if subse==subse[::-1]:
                d[mask]=len(subse)
        
        return max(d[mask1]*d[mask2] for mask1,mask2 in combinations(d,2) if mask1&mask2==0)