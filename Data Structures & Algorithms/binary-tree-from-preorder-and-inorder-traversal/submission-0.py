# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use indices and split up recursively
        # build indice map from inorder traversal.
        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i
        
        self.i = 0

        # pass in subtree dimensions from array sizes
        def dfs(len_start, len_end):
            if len_start > len_end:
                return

            node_val = preorder[self.i]

            self.i += 1
            mid = indices[node_val]

            node = TreeNode(node_val)
            node.left = dfs(len_start, mid - 1)
            node.right = dfs(mid + 1, len_end)

            return node

        
        return dfs(0, len(inorder) - 1)
