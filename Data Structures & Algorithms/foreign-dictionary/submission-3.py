class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        vertices: letters
        edges: (v, u) if u is lexographically ahead of v
        -- u has to show up ahead of v in output
        if cycle, return ""
        topological sort to make sure we dont prematurely add letters
        '''
        adj = { c: set() for w in words for c in w}
        for i in range(len(words) - 1): # pairs at a time
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # prefix is same but first is bigger -- invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            # find first differing character
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        
        seen, path = set(), set()
        res = []

        def dfs(v):
            # if v in path, that's a cycle
            print("path", path)
            print("seen", seen)
            print(v)
            if v in seen:
                return v in path
            
            path.add(v)
            seen.add(v)

            for u in adj[v]:
                if dfs(u):
                    return True

            path.remove(v)

            res.append(v)
        
        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
