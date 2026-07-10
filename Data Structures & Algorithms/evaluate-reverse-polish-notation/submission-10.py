from math import trunc

class Solution:
    def is_number(self, num: str) -> bool:
        try:
            int(num)
            return True
        except ValueError:
            return False

    def dispatch(self, first: int, second: int, token: str) -> int:
        if token == "+":
            return first + second
        elif token == "-":
            return first - second
        elif token == "*":
            return first * second
        else:
            return trunc(first / second)

    def evalRPN(self, tokens: List[str]) -> int:
        # store numbers on a stack
        # never put operations on stack
        # -- just use them when given.
        # can we map operations -> functions?

        # is it always valid? -- yes problem says so
        # which way does division go?

        # 22
        nums = []
        for token in tokens:
            if self.is_number(token):
                nums.append(int(token))
            else:
                second = nums.pop()
                first = nums.pop()
                print(first, token, second)
                print(6//-132)

                nums.append(self.dispatch(first, second, token))
        
        return nums[-1]