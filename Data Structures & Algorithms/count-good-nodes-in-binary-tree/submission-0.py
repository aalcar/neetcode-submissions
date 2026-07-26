# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # set max as youre going through
        # max gets backtracked as you go back up stack trace    
        count = 0

        def dfs(node, max_seen):
            if not node:
                return

            nonlocal count

            if max_seen <= node.val:
                max_seen = node.val
                count += 1

            dfs(node.left, max_seen)
            dfs(node.right, max_seen)

        dfs(root, float('-inf'))
        return count