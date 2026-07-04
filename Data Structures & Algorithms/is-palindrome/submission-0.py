class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.lower().replace(" ", "")

        left = 0
        right = len(stripped) - 1

        while left < right:
            if not stripped[left].isalnum():
                left += 1
                continue
            if not stripped[right].isalnum():
                right -= 1
                continue

            if stripped[left] != stripped[right]:
                return False
            
            left += 1
            right -= 1
        
        return True