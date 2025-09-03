class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod=int(1e9)+7
        arr=[1 for _ in range(10)]

        for _ in range(n-1):
            temp=[
                arr[4]+arr[6],
                arr[6]+arr[8],
                arr[7]+arr[9],
                arr[4]+arr[8],
                arr[3]+arr[9]+arr[0],
                0,
                arr[1]+arr[7]+arr[0],
                arr[2]+arr[6],
                arr[1]+arr[3],
                arr[2]+arr[4]
            ]
            arr=temp
        
        return sum(arr)%mod
        