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

# Recursion
- Time: O(n) -> binary search
- Space: This can vary between constant and O(n). The average and worst cases are O(n) because the queue size can scale with the number of nodes. However, the best case is that there can be n nodes, but 1 node per level. 
