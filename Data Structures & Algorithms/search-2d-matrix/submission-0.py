class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # it's sorted
        # requests O(log(m * n))
        # just treat it as a singular array and use a binary search
        # we can search over 0 -> m * n - 1
        # we can convert any index in the flattened matrix to
        # row & col with division and modulo
        # for any i in flattened, 
        # -- row = i // num_cols (n) 
        # -- col = i % n
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // n
            col = mid % n
            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False