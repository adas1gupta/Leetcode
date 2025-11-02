# Leetcode 752 - Open the Lock (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/open-the-lock/description/

## Notes: 
 - Shortest Distance to a target -> IMMEDIATELY THINK BFS
 - Use a visited set to reduce redundant work. For example, 0000 turns to 1000, and then back to 0000. 
 - For string manipulation and to turn 9 back into 0, use this code: num[:i] + str((int(num[i]) + 1) % 10) + num[i + 1:]

 - This is O(10000) time complexity and space complexity because there are only 10000 combinations that can be made with 0000. 

## Mistakes:
 - Remember to keep the visited.add line after you perform the check of the number not being in visited and not being in deadends


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)