class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_to_letters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return
            
            num = int(digits[i])
            for c in num_to_letters[num]:
                curr.append(c)
                backtrack(curr, i + 1)
                curr.pop()
            
        ans = []
        backtrack([], 0)
        return ans
                
    