class Solution:
    def isValid(self, s: str) -> bool:
        # have to deal with 3 types of parens
        # lets deal with simple case first
        # ex. [{{{}()}}]
        # it's always based on the last opening paren
        # If something is always based on the MOST RECENT thing
        # -- sounds like a stack question
        # [] we see [
        # we're monitoring for ] 
        # we're always monitoring for the specific closing paren
        # any opening paren is fine, because we have the chance to
        # see the specific closing paren at the end.
        # if we can't resolve all of the parens
        #   then the parens aren't valid
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        # [({}])
        # [(
        # 
        stack = []
        for c in s:
            if c in pairs: # O(1) see if it's opening
                stack.append(c)
                continue
            
            if stack and c == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
            
        return not stack
