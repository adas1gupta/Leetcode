# Leetcode 701 - Insert into a Binary Search Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

## Notes:
 - Follows the set left/right equal to the subtree pattern. 

 - Look for the spot by checking if value is < or > the current value.
  - Remember to return the node after you perform these checks so that the tree is continuously connected instead of having two unconnected trees. 
  
 - Eventually, when you reach None, return the new node with the value.

 - You're basically finding the next available spot in the tree that you can insert the value in, and the moment you encounter a None is when you insert. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 