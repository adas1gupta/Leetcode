# Leetcode 865 - Smallest Subtree with all the Deepest Nodes (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

## Notes:
 - Depth is collected from top down. 
    - The height pattern involves a return while the depth pattern involves passing in depth as an argument
 
 - Once you finish collecting the depth, each node needs to return the largest depth it's found because we're interested in the node(s) with the largest depth.
    - Given that, we need to record the max_depth as the max of itself and the depths that it finds between left and right. 
 - It's also important that the dfs function itself returns the depth for the base case because that will be the largest depth it can find.
    - And that it returns the max of the depths found at left and right because it is entirely possible that there is only 1 node with the largest depth instead of 2. 

 - Last thing is that we can't include a check if the lca is not already recorded.
 - This is because the lca is recorded at the leaf node, but it's entirely possible that there's another leaf node with the same max_depth. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 