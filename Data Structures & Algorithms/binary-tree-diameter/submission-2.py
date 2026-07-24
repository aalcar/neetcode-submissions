# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # track diameter and longest leg
        ans = 0
        def dfs(root):
            if not root:
                return 0

            nonlocal ans
            
            left = dfs(root.left)
            right = dfs(root.right)

            ans = max(ans, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return ans
