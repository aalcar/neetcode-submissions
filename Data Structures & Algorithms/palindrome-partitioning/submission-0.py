class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substr):
            l, r = 0, len(substr) - 1
            while l <= r:
                if substr[l] != substr[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        def backtrack(partition, i):
            if i == len(s):
                res.append(partition[:])
                return
        
            for j in range(i, len(s)):
                if is_palindrome(s[i:j + 1]):
                    partition.append(s[i:j + 1])
                    backtrack(partition, j + 1)
                    partition.pop()

        res = []
        backtrack([], 0)
        return res