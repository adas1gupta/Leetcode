from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        queue = deque(["0000"])

        levels = 0

        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                
                if num not in deadends and num not in visited:
                    for i in range(4):
                        queue.append(num[:i] + str((int(num[i]) + 1) % 10) + num[i + 1:])
                        queue.append(num[:i] + str((int(num[i]) - 1) % 10) + num[i + 1:])
                
                visited.add(num)

                if num == target: 
                    return levels

            levels += 1
        
        return -1
