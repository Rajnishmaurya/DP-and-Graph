class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)

        prefix=[float('-inf')]*n
        suffix=[float('-inf')]*n

        prefix[0]=arr[0]

        for i in range(1,n):
            prefix[i]=max(arr[i],prefix[i-1]+arr[i])
        
        suffix[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=max(arr[i],arr[i]+suffix[i+1])
        
        max_without_deletion=max(prefix)
        max_with_deletion=float('-inf')

        for i in range(1,n-1):
            max_with_deletion=max(max_with_deletion,prefix[i-1]+suffix[i+1])
        
        return max(max_with_deletion,max_without_deletion)
        