# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,value,root):
        if not root:
            root=TreeNode(value)
            return root
        if root.val>value:
            root.left=self.solve(value,root.left)
        else:
            root.right=self.solve(value,root.right)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root=TreeNode(preorder[0])
        n=len(preorder)
        for i in range(1,n):
            root=self.solve(preorder[i],root)
        return root
        