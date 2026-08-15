class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection with dfs
        # and adj list
        mp = defaultdict(list)
        for pre_req in prerequisites:
            mp[pre_req[0]].append(pre_req[1])

        # needs to be current recursive path
        # to know its a cycle
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if not mp[course]:
                return True

            visiting.add(course)

            for pre_req in mp[course]:
                if not dfs(pre_req):
                    return False
            
            visiting.remove(course)
            mp[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        
        