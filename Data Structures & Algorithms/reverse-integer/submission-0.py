class Solution:
    def reverse(self, x: int) -> int:
        # get a digit
        # if it causes overflow, go to 0
        # put the digit into result and push it forward
        MAX = 2 ** 31 - 1
        MIN = -(2 ** 31)
        res = 0

        # use casts and fmod to truncate instead of floor division
        # ex. if floor division, -3.5 goes to -4
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            # if max is 975005
            # ex. x=98000
            # if we mult by 10, it goes over
            # ex. x=97500
            # we need more info, what about last digit?
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            res = (res * 10) + digit
    
        return res