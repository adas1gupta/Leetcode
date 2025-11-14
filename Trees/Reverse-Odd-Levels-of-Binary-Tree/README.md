# Leetcode 2415 - Reverse Odd Levels of Binary Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

## Notes:

# BFS
 - Remember that a collection of objects stores references/pointers to the objects instead of copies to them. 
 - This is what enables you to use a list(queue). 
 - You create a list so that you can index in O(1) time. 
 - Deque indexing is O(n) time. 

 - Just swap when on odd level using two pointers. Don't pop just yet for simplicity. 
 - Then, go through the queue and continue processing level by level.
 - We go through the queue with the order actually maintained because the values were simply swapped within the list and that changes the objects that are in the queue.
    - Therefore, there's no need to maintain any complex ordering logic. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 