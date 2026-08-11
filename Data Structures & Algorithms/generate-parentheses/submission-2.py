class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, count):
            if len(curr) == 2 * n:
                if count == 0:
                    res.append("".join(curr))
                return
        
            # count = opening - closing
            # len = opening + closing
            # add together and divide by two
            open_count = (len(curr) + count) // 2
            if count < 0 or open_count > n:
                return
            
            curr.append('(')
            backtrack(curr, count + 1)
            curr.pop()

            curr.append(')')
            backtrack(curr, count - 1)
            curr.pop()

        backtrack([], 0)
        return res