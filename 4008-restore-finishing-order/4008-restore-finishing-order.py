class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans=[]
        for i in range(len(order)):
            if order[i] in friends:
                ans.append(order[i])
        return ans
        