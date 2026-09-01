class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)
        for src, dst in tickets[::-1]:
            adj[src].append(dst)

        curr_path = ["JFK"]
        res = []

        while curr_path:
            curr = curr_path[-1]
            if adj[curr]:
                curr_path.append(adj[curr].pop())
            else:
                res.append(curr_path.pop())

        return res[::-1]