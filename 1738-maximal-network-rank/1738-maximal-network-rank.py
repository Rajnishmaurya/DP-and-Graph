class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        indegree=[0]*n
        connected=set()
        for x,y in roads:
            indegree[x]+=1
            indegree[y]+=1
            connected.add((x,y))
            connected.add((y,x))

        result=0
        for i in range(n):
            for j in range(i+1,n):
                rank=indegree[i]+indegree[j]
                if (i,j) in connected:
                    rank-=1
                result=max(result,rank)
        return result
        