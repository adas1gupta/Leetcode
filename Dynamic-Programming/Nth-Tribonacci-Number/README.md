# Leetcode 746 - Min Cost Climbing Stairs (Easy)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/min-cost-climbing-stairs/

## Notes: 
 - This is bottom-up DP because the base cases at the bottom of the tree are N(0), N(1), and N(2). 

 - Those base cases aren't at the top of the tree. 

 - There are cases where n = 0, so make sure to handle cases where n is already at one of the base cases. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)