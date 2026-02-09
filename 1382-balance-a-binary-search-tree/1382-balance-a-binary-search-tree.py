# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node, vals):
            if not node:
                return

            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)

        def buildTree(vals, left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(vals[mid])
            node.left = buildTree(vals, left, mid - 1)
            node.right = buildTree(vals, mid + 1, right)
            return node

        vals = []
        inorder(root, vals)
        return buildTree(vals, 0, len(vals) - 1)