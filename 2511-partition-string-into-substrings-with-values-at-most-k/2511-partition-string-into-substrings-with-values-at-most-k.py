class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        current=0
        ans=1

        for d in s:
            if int(d)>k:
                return -1
            
            current=10*current+int(d)
            if current>k:
                ans+=1
                current=int(d)
        return ans
        