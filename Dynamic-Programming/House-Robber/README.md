# Leetcode 198 - House Robber (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/house-robber/description/

## Notes: 
 - Recurrence relation hypothesis: determine your choices at state i. 

 - Here, your choices are to take the current position and look two positions forward. 
 - Or recalculate the above, but for the next position. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)