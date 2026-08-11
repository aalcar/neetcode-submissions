class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, count):
            if len(curr) == 2 * n:
                if count == 0:
                    res.append("".join(curr))
                return
            
            if count < 0:
                return
            
            curr.append('(')
            backtrack(curr, count + 1)
            curr.pop()

            curr.append(')')
            backtrack(curr, count - 1)
            curr.pop()

        backtrack([], 0)
        return res