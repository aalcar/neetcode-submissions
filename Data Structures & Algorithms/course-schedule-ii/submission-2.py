class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort | kahns
        # inorder[crs] = 0 means no pre-reqs
        inorder = defaultdict(int)
        mp = defaultdict(list)
        q = deque()
        res = []

        for crs, pre in prerequisites:
            inorder[pre] += 1
            mp[crs].append(pre)
        
        for crs in range(numCourses):
            if not inorder[crs]:
                q.append(crs)

        while q:
            crs = q.popleft()
            res.append(crs)

            for pre_req in mp[crs]:
                inorder[pre_req] -= 1
                if not inorder[pre_req]:
                    q.append(pre_req)

        if len(res) != numCourses:
            return []

        res.reverse()
        return res
