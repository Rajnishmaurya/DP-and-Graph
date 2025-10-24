class DSU:
    def __init__(self):
        self.parent={}
    
    def find(self,x):
        if x not in self.parent:
            self.parent[x]=x
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ds=DSU()

        for x,y in stones:
            ds.union(x,y+10001)
        
        components=set()

        for x,y in stones:
            components.add(ds.find(x))
            components.add(ds.find(y + 10001))
        
        return len(stones)-len(components)
        