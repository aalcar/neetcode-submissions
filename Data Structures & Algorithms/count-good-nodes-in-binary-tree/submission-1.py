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
        # use dfs to track the count  
        def dfs(node, max_seen):
            if not node:
                return 0

            count = 0
            if max_seen <= node.val:
                max_seen = node.val
                count = 1

            count += dfs(node.left, max_seen)
            count += dfs(node.right, max_seen)

            return count

        
        return dfs(root, float('-inf'))