class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        st=set(arr)
        for i in range(1,1000000):
            if i not in st:
                k-=1
                if k==0:
                    return i
                
        