# Leetcode 298 - Binary Tree Longest Consecutive Sequence (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/

## Notes: 
 - Keep track of the maximum length.
 - Keep track of the previous to compare current node's value with previous.
 - Reset the length if the current node is not +1 to prev. 
 - Update max_length.
 - Call dfs on left and right

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> explore all the nodes
- Space: This can vary between constant and O(n). The average and worst cases are O(n) because the queue size can scale with the number of nodes. However, the best case is that there can be n nodes, but 1 node per level. 
