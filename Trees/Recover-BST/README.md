# Leetcode 99 - Recover Binary Search Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/recover-binary-search-tree/description/

## Notes:
 - Think of this problem like an array. 
 
 - [1, 6, 3, 4, 2] Basically, the nodes I should be swapping are 6 and 2.
    - The first violation is when the prev is less than the current.
    - That element should be anchored.
 - The second violation is when the current is less than prev.
    - That's the second element to swap with. 
 
 - This piece of code if not first: first = prev

 - Then you can do if first and curr > prev: second = curr

 - We are expecting that during an inorder traversal, every node will be greater than the one previous to it. 
 - However, when we see a node that isn't greater than, it means that:
   - The first occurrence is when the previous node is the violating node. 
 - The moment that node is found, then the second occurrence is when the current node is less than the previous node. 
   - The current node is then the violating node. 

## Mistakes:
 - When you change prev between the checks for first and second, you're changing what prev points to for the calculation for no reason.
 - Keep it consistent. Keep it pushing p!


## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 