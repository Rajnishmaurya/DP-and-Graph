class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[1]*5
        mod=int(1e9)+7

        for _ in range(n-1):
            temp=[
                arr[1],
                arr[0]+arr[2],
                arr[0]+arr[1]+arr[3]+arr[4],
                arr[2]+arr[4],
                arr[0]
            ]
            arr=temp

        return sum(arr)%mod
