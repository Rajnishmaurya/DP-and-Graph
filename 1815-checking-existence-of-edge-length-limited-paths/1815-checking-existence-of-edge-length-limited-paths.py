class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)

        if x!=y:
            if self.rank[x]<self.rank[y]:
                self.parent[x]=y
            elif self.rank[x]>self.rank[y]:
                self.parent[y]=x
            else:
                self.parent[x]=y
                self.rank[y]+=1

class Solution:
    def sorter(self,val):
        return val[2]
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        for i ,q in enumerate(queries):
            queries[i].append(i)
        queries.sort(key=self.sorter)
        edgeList.sort(key=self.sorter)

        i=0
        ans=[False]*len(queries)
        uf=DSU(n)
        for q in queries:
            while i<len(edgeList) and edgeList[i][2]<q[2]:
                uf.union(edgeList[i][0],edgeList[i][1])
                i+=1
            
            if uf.find(q[0])==uf.find(q[1]):
                ans[q[3]]=True
        return ans


        
        
        