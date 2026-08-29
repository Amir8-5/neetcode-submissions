# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif not q or not p:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        equal = self.equalNode(p, q)
        print(f"p and q are: {p.val} and {q.val}")
        print(equal, left, right)
        return equal and left and right

    def equalNode(self, p, q):
        if not p or not q:
            return False
        return p.val == q.val

        