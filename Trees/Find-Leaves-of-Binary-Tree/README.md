# Leetcode 366 - Find Leaves of Binary Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/find-leaves-of-binary-tree/description/

## Notes:
 - The nodes that are actually leaves at point x is actually determined by their height, or how many nodes are between them and None. 
    - Depth is from root to node while height is from the None beyond leaf to node. 
 
 - Use your dfs to calculate height. 
 - Take the maximum height from left or right. 
    - This is because the maximum height actually represents the true height of the node (Just think about it)
 
 - Then, update the levels hashmap to append that node at that height. 
 - Then, return the max height. 

# Mistakes
 - Important to remember that when collecting height, we need to return the max of the left and right heights to find the actual height associated with a given node.  

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 