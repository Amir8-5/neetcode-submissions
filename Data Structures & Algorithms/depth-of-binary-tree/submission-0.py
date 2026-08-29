# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if self.isEmpty(root):
            return 1

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(1+leftDepth, 1+rightDepth)

    def isEmpty(self, root):
        if root.left is None and root.right is None:
            return True
        else:
            return False
        