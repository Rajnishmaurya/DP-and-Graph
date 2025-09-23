class Solution:
    def solve(self,index,nums,temp,ans):
        if index==len(nums):
            temp.sort()
            ans.add(tuple(temp))
            return
        temp.append(nums[index])
        self.solve(index+1, nums,temp,ans)
        temp.pop()
        self.solve(index+1,nums,temp,ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        temp=[]
        self.solve(0,nums,temp,ans)
        result=[]
        for it in ans:
            result.append(list(it))
        return result
        