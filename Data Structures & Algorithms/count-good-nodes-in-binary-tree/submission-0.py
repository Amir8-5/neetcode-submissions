# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def dfs(root, maxim):
            nonlocal res
            if not root:
                print("none root")
                return 
            if root.val >= maxim:
                res += 1
                maxim = root.val
            print(f"root is : {root.val}, res is: {res}, max is: {maxim}")
            right = dfs(root.right, maxim)
            left = dfs(root.left, maxim)
            return
        
        dfs(root, root.val)
        return res
        