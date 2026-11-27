# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        When we delete a node,
        - We want to replace it with the leftmost node in the right subtree
        """

        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # we found correct node
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            cur = root.right
            while cur.left:
                cur = cur.left
            # we've arrived at the in-order successor
            root.val = cur.val
            # we've copied the value so now we delete the node to the right with val
            root.right = self.deleteNode(root.right, root.val)
    
        return root