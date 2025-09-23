class Solution:
    def solve(self,index,target,candidates,temp,ans):
        if index>=len(candidates):
            if target==0:
                ans.append(temp[:])
            return
        self.solve(index+1,target,candidates,temp,ans)
        if candidates[index]<=target:
            temp.append(candidates[index])
            self.solve(index,target-candidates[index],candidates,temp,ans)
            temp.pop()
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        self.solve(0,target,candidates,temp,ans)
        return ans
        