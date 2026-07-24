# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # find longest path on the left and add to longest path on right
        # doesnr work
        max_diameter = 0
        def dfs(root):
            nonlocal max_diameter

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)

        dfs(root)

        return max_diameter