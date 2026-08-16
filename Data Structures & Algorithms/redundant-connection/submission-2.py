class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # do one dfs
        # rewind recursion when cycle is reached
        # mark any node on that path until the
        # node that was visited 2x is seen again
        # then iterate reverse of edges 
        # and return first pair thats in your cycle_path
        visited = set()
        cycle_path = set()
        cycle_start = -1
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, parent):
            nonlocal cycle_start

            if node in visited:
                cycle_start = node
                return True
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                
                if dfs(neighbor, node):
                    if cycle_start != -1:
                        cycle_path.add(node)
                    if node == cycle_start:
                        cycle_start = -1

                    return True

            return False
 
        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle_path and v in cycle_path:
                return [u, v]

        return []