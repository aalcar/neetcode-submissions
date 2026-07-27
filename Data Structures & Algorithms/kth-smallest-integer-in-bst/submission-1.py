# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do in-order traversal
        # and index the kth element
        count = 0
        ans = root.val
        def dfs(node):
            if not node:
                return

            nonlocal count, ans
            
            left = dfs(node.left)

            if count == k:
                return
            
            count += 1

            if count == k:
                ans = node.val
                return
            
            right = dfs(node.right)

        dfs(root)
        return ans