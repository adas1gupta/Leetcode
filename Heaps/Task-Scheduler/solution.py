from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-freq for freq in task_counts.values()]
        heapq.heapify(max_heap)
        cooldown = deque()

        current_time = 0

        while max_heap or cooldown:
            if cooldown and cooldown[0][1] == current_time:
                pop = cooldown.popleft()
                heapq.heappush(max_heap, -pop[0])
            
            if max_heap:
                count = -(heapq.heappop(max_heap)) - 1
                if count != 0:
                    cooldown.append((count, current_time + n + 1))
            
            current_time += 1
        
        return current_time