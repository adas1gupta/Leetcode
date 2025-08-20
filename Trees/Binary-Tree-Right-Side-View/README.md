# Leetcode 199 - Binary Tree Right Side View (Medium)

**Topic**: Tree, BFS
**Link**: https://leetcode.com/problems/binary-tree-right-side-view/description/

## Notes: 
 - Have a result list
 - Do the typical bfs setup. 
 - Check if root is empty. 
 - Here's the tricky part:
    - The current approach is that you pile all the nodes, and then when you pop the last node, that'll be the right node.
    - As a result, you check if the length of the queue is equal to 0, and if it is, append it to the result. 
    - However, there are test cases where there are right children from the left side, and since the left side is processed first, nodes from future levels are being added. 
    - This messes up calculations for the current level. 
    - A simple fix to that is simply creating a new queue for the next level and adding the children to that queue. 
        - After that, just set the outer queue equal to the new queue. 
 - 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) -> explore all the nodes. 
- Space: O(h) -> height of the tree is the amount of space stored for the call stack