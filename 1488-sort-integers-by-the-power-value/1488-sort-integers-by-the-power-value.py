class Solution:
    def solve(self, num,count):
        if num==1:
            return count
        elif num%2==0:
            return self.solve(num//2,count+1)
        else:
            return self.solve(3*num+1,count+1)

    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic={}

        for i in range(lo,hi+1):
            temp=self.solve(i,0)
            dic[i]=temp
        
        sorted_values=sorted(dic.items(),key=lambda x:x[1])
        return sorted_values[k-1][0]
        