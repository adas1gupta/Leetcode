from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque([])
        self.top_element = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top_element = x

    def pop(self) -> int:
        n = len(self.stack)
        while n > 1:
            self.top_element = self.stack.popleft()
            self.stack.append(self.top_element)
            n -= 1

        return self.stack.popleft()

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()