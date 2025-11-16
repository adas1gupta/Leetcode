# Leetcode 236 - Lowest Common Ancestor of a Binary Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

## Notes:

# BFS
 - Left subtree checks if any of the values yielded either p or q. 
    - Yes, left can yield q.
 - Right also does the same. 
 
 - Then, you have to check both the right and left subtrees to see if p was found + the current node.
 - The same thing for right.
 
 - Then, if lowest common ancestor is set to None and both are found, set lowest common ancestor to current node

 - Return these checks above in an array:
    - Then, you have to check both the right and left subtrees to see if p was found + the current node.
    - The same thing for right.
   
 - Just think about this recursively. 
 - What do you want to yield from the each subnode of a tree? 
   - Whether they have found p or found q? 
 - So just figure out what to return.
   - If Node is none, that means p nor q were able to be found.
   - So just return [False, False]
 - Then, think about what to return past None or leaf node. 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 