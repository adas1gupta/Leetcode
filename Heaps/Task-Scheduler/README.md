# Leetcode 621 - Task Scheduler (Medium)

**Topic**: Heaps
**Link**: https://leetcode.com/problems/task-scheduler/description/

## Notes: 
 - Basically, you can’t repeat the tasks, so you have to be efficient. 
    - Set of tasks: AAABBCC, n = 1 (can’t immediately repeat)
    - Efficient way to complete it is: ABACABC
 - A key observation is that you always want the most frequent element to come first. 
 - To efficiently get the most frequent element, use a max heap. 
 - You use a queue to keep track of the cooldown of tasks
    - Every time you pop a task from the heap, decrement its frequency, and if it’s not 0, enqueue it with the time it’s next available (current_time + n). 
    - Before popping from the heap, there’s always the edge case that the front task has just met its cooldown, so it should be added in case it still has the max frequency. 
 - Use a Counter to acquire the frequencies. 
 - Create a max_heap of the Counter’s values, and heapify it. 
 - Create a queue for the cooldowns. 
 - Create a current_time counter and set it to 0. 
 - The while condition is while you have frequencies or cooldowns left because frequencies can be empty while there are items left in the queue that can potentially be added back to the frequency max heap. 

## Mistakes:
 - The algorithm is to keep popping the max_count, and then record the next time it's available using a queue because the cooldown that will appear earlier will enter the queue earlier, so popping left becomes efficient.


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(m)
- Space: O(1)