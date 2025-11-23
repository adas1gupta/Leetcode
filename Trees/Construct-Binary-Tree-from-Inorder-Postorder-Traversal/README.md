# Leetcode 106 - Construct Binary Tree from Inorder and Postorder Traversal (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

## Notes:
 - Use a hashmap to quickly find the index of a value. 

 - Get the value to process from postorder. 
 - Find the index of the value in the inorder array to partition.
 
 - Process the right first because you'll encounter the rightmost elements first in the postorder array.
 - If you do node.left first, then the right elements will become the left tree of node. 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 