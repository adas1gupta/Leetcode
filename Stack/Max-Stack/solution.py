import heapq

class MaxStack:

    def __init__(self):
        self.max_heap = []
        self.stack = []
        self.removed = set()
        self.unique_id = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (x * -1, -self.unique_id))
        self.stack.append((x, self.unique_id))
        self.unique_id += 1

    def pop(self) -> int:
        while self.stack[-1][1] in self.removed:
            self.stack.pop()
        
        to_return, remove_id = self.stack.pop()
        self.removed.add(remove_id * -1)

        return to_return

    def top(self) -> int:
        while self.stack[-1][1] in self.removed:
            self.stack.pop()

        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.max_heap[0][1] in self.removed:
            heapq.heappop(self.max_heap)
            
        return self.max_heap[0][0] * -1

    def popMax(self) -> int:
        while self.max_heap[0][1] in self.removed:
            heapq.heappop(self.max_heap)
        
        to_pop, removed_id = heapq.heappop(self.max_heap)
        self.removed.add(removed_id * -1)
        
        return to_pop * -1

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()