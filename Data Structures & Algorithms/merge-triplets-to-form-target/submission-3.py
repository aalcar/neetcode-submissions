class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # we want our triplet to be the max
        # get rid of everything where a > t_a or b > t_b or c > t_c
        t_a, t_b, t_c = target
        max_a = max_b = max_c = float('-inf')

        for a, b, c in triplets:
            if a > t_a or b > t_b or c > t_c:
                continue
            
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)

        return t_a == max_a and t_b == max_b and t_c == max_c