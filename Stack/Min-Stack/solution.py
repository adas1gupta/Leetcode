class MinStack:

    def __init__(self):
        self.stack = []
        self.curr = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append(val)
        self.curr.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.curr.pop()
        self.min = self.curr[-1] if len(self.curr) > 0 else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()