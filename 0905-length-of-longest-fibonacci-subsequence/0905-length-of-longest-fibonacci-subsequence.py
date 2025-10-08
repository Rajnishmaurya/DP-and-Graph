class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)

        dp=[[0]*n for _ in range(n)]

        max_len=0
        for curr in range(2,n):
            start,end=0,curr-1
            while start<end:
                temp=arr[start]+arr[end]
                if temp>arr[curr]:
                    end-=1
                elif temp<arr[curr]:
                    start+=1
                else:
                    dp[end][curr]=dp[start][end]+1
                    max_len=max(max_len,dp[end][curr])
                    start+=1
                    end-=1
        return 0 if max_len==0 else max_len+2
             

        