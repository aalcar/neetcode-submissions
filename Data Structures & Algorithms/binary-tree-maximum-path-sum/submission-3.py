# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        # return sum of subtree?
        def dfs(root):
            if not root:
                return 0

            nonlocal max_sum

            left = dfs(root.left)
            right = dfs(root.right)

            # curr_sum = root.val + max(left, right)

            # return max including the branch not followed
            max_sum = max(root.val + left + right, max_sum)
            
            return max(root.val + max(left, right), 0)

        dfs(root)
        return max_sum