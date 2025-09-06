class UnionFind:
    def __init__(self):
        self.parent=[i for i in range(26)]
        self.rank=[1]*26
    
    def find(self,s):
        if self.parent[s]!=s:
            self.parent[s]=self.find(self.parent[s])
        return self.parent[s]
    
    def union(self,i,j):
        x=self.find(i)
        y=self.find(j)

        if x!=y:
            if self.rank[x]>self.rank[y]:
                self.parent[y]=x
            elif self.rank[x]<self.rank[y]:
                self.parent[x]=y
            else:
                self.parent[x]=y
                self.rank[y]+=1
    def connected(self,i,j):
        return self.find(i)==self.find(j)
    

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf=UnionFind()

        for eq in equations:
            if eq[1]=='=':
                x,y=ord(eq[0])-ord('a'),ord(eq[-1])-ord('a')
                uf.union(x,y)
            # if eq[1]=='!':
            #     x,y=ord(eq[0])-ord('a'),ord(eq[-1])-ord('a')
            #     if uf.connected(x,y):
            #         return False
        for eq in equations:
            # if eq[1]=='=':
            #     x,y=ord(eq[0])-ord('a'),ord(eq[-1])-ord('a')
            #     uf.union(x,y)
            if eq[1]=='!':
                x,y=ord(eq[0])-ord('a'),ord(eq[-1])-ord('a')
                if uf.connected(x,y):
                    return False
        return True
        