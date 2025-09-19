from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.window = deque([])
        self.max_len = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.window) >= self.max_len:
            self.total -= self.window.popleft()
        self.window.append(val)
        self.total += val

        return self.total / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)