class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # so at most n boats
        # at min... n / 2
        people.sort()
        l, r = 0, len(people) - 1
        count = 0
        while l <= r:
            # 1,2,4,5
            # 1,2,2,3,3
            # 1,2,3,4,5,6 limit = 8
            # 2,3,4,5
            # 2,5,7,9,10,13,15,19, limit=21
            # 5,7,9,10,13,15
            # 7,9,10,13
            # 9,10
            # 1,2,2,3,3
            if people[l] + people[r] > limit:
                count += 1
                r -= 1
                continue
            
            l += 1
            r -= 1
            count += 1

        return count
