# Leetcode 198 - House Robber (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/house-robber/description/

## Notes: 
 - The end of the array can't loop back to the beginning because if you choose 0 or 1 and go to the second to last element, you cannot go back to 0.
 - This is because 0 is next to 1, which violates the adjacency rule.
 - Why this problem is different is that the last element is now next to the first element, and robbing both will violate the adjacency rule. 

 - The idea is that you apply the house robber solution to two parts of the array, one from 0 to 2nd to last and the other from 1 to last. 
 - Pass in a separate memo for each and take the maximum of the results of dp on both arrays. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)