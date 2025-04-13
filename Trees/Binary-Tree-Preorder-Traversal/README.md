# Leetcode 102 - Binary Tree Preorder Traversal (Easy)

**Topic**: Tree
**Link**: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

## Notes: 
 - helper recursive function
    - append the value of the node to the result list
    - explore left path until you reach None
        - return in the case of None
    - explore right path
 - call helper on root
 - return result list

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) -> explore all the nodes
- Space: O(h) -> height of the tree is the amount of space stored for the call stack
         O(n) -> if result list is being factored in. 

