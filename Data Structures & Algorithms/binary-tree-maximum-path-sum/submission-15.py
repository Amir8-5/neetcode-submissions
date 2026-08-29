# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -9999

        def dfs(root):
            nonlocal maxSum
            if not root:
                return [-9999, -9999]
            if not root.left and not root.right:
                print(f"not left and right: {root.val}")
                maxSum = max(maxSum, root.val)
                return [root.val, root.val]
            # left = [max(num, 0) for num in dfs(root.left)]
            left = dfs(root.left)
            # right = [max(num, 0) for num in dfs(root.right)]
            right = dfs(root.right)
            withRoot = max(left[1] + right[1] + root.val, root.val )
            without = max(root.val, left[1] + root.val, right[1] + root.val)
            maxSum = max(withRoot, without, maxSum)
            print(f"begin:\nleft: {left}\nright: {right}\nwith: {withRoot}\nwithout: {without}\nmax:{maxSum}\nend")
            return [withRoot, without]
        dfs(root)
        return maxSum