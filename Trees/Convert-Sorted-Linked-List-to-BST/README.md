# Leetcode 109 - Convert Sorted List to Binary Search Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

## Notes:
 - Inorder is left, root, right. 

 - Inorder traversal goes all the way left, and head points to the first node, so the first node will be the left value.
 - Then it'll go back to root and the second node will be the second value.
 - Then right will be the third value, and it'll pop back up.

 - We need to know what the middle value is so that we can split the "array" in half multiple times into their left and right trees.

 - How this works is that we basically recurse until we reach the first node. 
    - (0, 5) -> 3
    - (0, 2) -> 1
    - (0, 1) -> 0
    - (0, -1) -> Return None
    - (0, 1) -> Now we form the node and that will be the left of (0, 2)
 - Once we reach the leftmost node, that's where the first value will go.
 - Then, we actually make the value and try to form the right tree.
 - Then, we return, and the left tree is fully formed.

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 