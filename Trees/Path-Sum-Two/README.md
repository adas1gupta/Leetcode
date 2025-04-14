# Leetcode 113 - Path Sum II (Medium)

**Topic**: Tree
**Link**: https://leetcode.com/problems/path-sum-ii/description/

## Notes: 
 - have a result list
 - have a helper recursive function that takes in the node, path array, and current sum of path
    - use the typical structure associated with leaf node questions.
        - if not node, return.
        - Some sort of code: in this case, adding the node.val to the current_sum variable and the path array. 
        - checking if it's a leaf node, and if it is, compare current_sum to target_sum. 
            - If they match, append a copy of the path array to the result list. 
            - Pop from the path array, and return. 
        - Then, figure out when to call helper, and in this case, you can call helper on both freely because of the if not node base case taking care of the cases where the binary tree isn't complete.
 - Call the helper on the root, empty array, and 0.
 - Return the result list. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) -> explore all the nodes. 
- Space: O(h) -> height of the tree is the amount of space stored for the call stack