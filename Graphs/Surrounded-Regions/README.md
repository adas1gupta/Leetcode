# Leetcode 130 - Surrounded Regions (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/surrounded-regions/description/

## Notes: 
 - Honestly, the hard part is realizing that the only Os that can remain are the ones starting from the shore (sides of the grid). 

 - Afterwards, the next key insight it just turning those Os into Ts so that you can perform 1 pass and turn remaining Os into Xs and the 2nd pass to turn Ts back into Os. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)