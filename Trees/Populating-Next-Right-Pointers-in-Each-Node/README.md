# Leetcode 116 - Populating Next Right Pointers in Each Node (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

## Notes:
 - You're connecting nodes within the same level to the node after it.
 
 - Could do this with BFS.
 - DFS approach is also possible

## DFS:
 - There's guaranteed to be 2 children.
 - If there is a left child, connect it to the right child
 - If there is a right child, check if the parent node is connected to someone.
    - If it is, connect the right child to the next's left child. 
    - Just imagine it

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 