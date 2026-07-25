# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        it's a BST
        all nodes are unique
        and we can search efficienctly

        we can get values of p and q and find the node no?
        or atleast find direction
        for a given node, can be:
        -- larger than both p and q
            -- search left subtree
        -- smaller than both p and q
            -- search right subtree
        -- >= one and <= the another
        --    return
        -- 
        """
        curr = root.val
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root