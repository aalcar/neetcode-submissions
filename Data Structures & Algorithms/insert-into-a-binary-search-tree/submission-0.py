# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        if val > node:
            if not node.right:
                place here
            recurse
            insert into right
        """
        if not root:
            return TreeNode(val)

        def dfs(node, val):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right, val)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    dfs(node.left, val)

        dfs(root, val)
        return root