# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root.left==None and root.right==None:
            return 0
        q=deque()

        if root.left:
            q.append((root.left,'l',1))
        if root.right:
            q.append((root.right,'r',1))
        
        ans=0

        while q:
            node,direction,step=q.popleft()
            ans=max(ans,step)

            if node.left:
                if direction=='l':
                    q.append((node.left,'l',1))
                if direction=='r':
                    q.append((node.left,'l',step+1))
            if node.right:
                if direction=='r':
                    q.append((node.right,'r',1))
                if direction=='l':
                    q.append((node.right,'r',step+1))
        return ans
        