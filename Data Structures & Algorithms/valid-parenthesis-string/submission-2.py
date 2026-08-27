class Solution:
    def checkValidString(self, s: str) -> bool:
        # track minimum and maximum amount of open left parans possible
        leftMax = leftMin = 0
        for c in s:
            if c == '(':
                leftMax += 1
                leftMin += 1
            elif c == ')':
                leftMax -= 1
                leftMin -= 1
            else:
                leftMax += 1
                leftMin -= 1
            
            if leftMax < 0:
                return False

            if leftMin == -1:
                leftMin = 0
        
        return leftMin == 0