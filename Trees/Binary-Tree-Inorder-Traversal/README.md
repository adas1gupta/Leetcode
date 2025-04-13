# Leetcode 102 - Binary Tree Inorder Traversal (Easy)

**Topic**: Tree
**Link**: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

## Notes: 
 - helper recursive function
    - explore left path until you reach None
        - return in that case
    - append the value of the node to the result list
    - explore right path
 - call helper on root
 - return result list

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) -> explore all the nodes
- Space: O(h) -> height of the tree is the amount of space stored for the call stack
         O(n) -> if result list is being factored in. 

