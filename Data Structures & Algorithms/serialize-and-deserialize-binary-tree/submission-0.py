# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        What would we want to export for example 1 and 2?
        ex1:
        1$2$N$N$3$4$N$N$5$N$N$
        ex2:
        N$
        """
        res = []

        def dfs(root): # preorder
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_vals = data.split(',')

        self.i = 0

        def dfs():
            if node_vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(node_vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()