class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # just maintain global visited set
        # dfs on everything
        # return early on visited
        # count
        visited = set()
        count = 0
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, parent):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue

                dfs(neighbor, node)
        
        for i in range(n):
            if i in visited:
                continue
            
            dfs(i, -1)
            count += 1

        return count