# Leetcode 102 - Binary Tree Level Order Traversal (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## Notes: 
 - Take care of the empty input because when you do deque([root]), the deque contains [[]], which is length one. 
 - Deque expects to be initialized with a container (similar to listifying anything with list -> it expects a container to listify)
 - while the queue still has items in it
    - Create a level array to append items from the current level to this array. This array will then be appended to the result array after the for loop concludes.  
    - Measure the length of the current queue, and that's the length of the current level. 
    - for _ in range(len(queue)) -> Loop through how long the level is supposed to be. 
        - Don't do (for item in queue) because when items are popped from the queue, it'll cause issues. 
        - Pop the node and append the value to the level. 
        - If the node you popped has a left node, append it to the queue.
        - If it has a right node, append it to the queue. 
    - After the for loop, append the entire level array to the result list. 
 - return the result list. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> explore all the nodes
- Space: This can vary between constant and O(n). The average and worst cases are O(n) because the queue size can scale with the number of nodes. However, the best case is that there can be n nodes, but 1 node per level. 
