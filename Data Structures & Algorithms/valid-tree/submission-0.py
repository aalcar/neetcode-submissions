class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # turn into adjacency list?
        adj_list = defaultdict(set)
        visited = set()

        for node, neighbor in edges:
            adj_list[node].add(neighbor)
            adj_list[neighbor].add(node)

        # there cant be a cycle.
        # not sure if there's other issues?
        # just do a dfs bro
        # oh i see
        # temporarily get rid of back edge?

        # track the parent so i dont have to remove back edge
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n

