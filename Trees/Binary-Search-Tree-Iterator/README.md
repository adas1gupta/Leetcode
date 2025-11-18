# Leetcode 173 - Binary Search Tree Iterator (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/binary-search-tree-iterator/description/

## Notes:
 - A BST in sorted order is done using inorder traversal.
    - Inorder traversal is Left, Root, Right.

 - You want to dfs the left side first using this code:
    - while node: add to the stack, go to node.left
 - At the end of this, you'll have (from top of stack to bottom) [leaf of left, parent of leaf, so on and so forth until root]
    - Leaf nodes are at the top of the stack.
 
 - Then, when you pop off with next, there's 2 scenarios that can occur. 
    - One is that the leftmost node isn't actually the leaf node, and the nodes to the right are the leaf nodes.
 - In that case, you still want to return the left node because the inorder traversal is leftmost (None), root (leftmost node), right (right).
    - The other is that you pop left and reach root.
    - You still return root because of inorder traversal, but you want to explore right
    - So call dfs on the top_node.right
 
 - The entire point of lazily evaluating versus evaluating at initialization is that the stack is O(h) instead of O(n)


## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 