class MinStack:
    # just track the minimum value?
    # how do we know when we pop it off...
    # oh do we have two stacks.?
    # how do we keep track of the min elements
    # this is definitely a defer until later problem

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    # in stack: 10 9 11 13 8 14 15 16
    # min vals: 10 9 9  9  8 8  8  8
    # just keep a monotonic min stack
    # if there's a smaller val before a bigger one, we know the bigger
    # one can NEVER be the min
    def getMin(self) -> int:
        return self.mins[-1]

        
