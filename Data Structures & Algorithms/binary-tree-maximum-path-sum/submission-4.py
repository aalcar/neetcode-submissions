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

            max_leg_sum = max(left, right)
            min_leg_sum = min(left, right)
            current_subtree_sum = root.val + left + right

            # return max including the branch not followed
            max_sum = max(current_subtree_sum, max_sum)
            
            return max(root.val + max_leg_sum, 0)

        dfs(root)
        return max_sum