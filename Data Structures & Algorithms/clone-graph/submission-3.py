"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create adj list
        # iterate through list
        # make nodes
        # why not just make nodes from current..
        # we need to make all the nodes first then add neighbors?
        # val to neighbor dict?
        if not node:
            return None

        old_to_new = {node: Node(node.val)}

        q = deque([node])

        while q:
            q_len = len(q)

            for _ in range(q_len):
                curr = q.popleft()
        
                for neighbor in curr.neighbors:
                    if neighbor not in old_to_new:
                        old_to_new[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]