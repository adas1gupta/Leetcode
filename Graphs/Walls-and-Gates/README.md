# Leetcode 286 - Walls and Gates (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/walls-and-gates/description/

## Notes: 
 - First thing that should immediately occur to you is that this problem is multi-source. 
 - First piece of intuition is that you might want to start from a room and see how far it is from a gate.
    - However, the way you should be doing this is that you should start from a gate and see how far each room is from it. 
 - Once you realize that this is multi-source, IMMEDIATELY THINK OF BFS. 

 - There are two ways to approach multi-source:
 - Either you start from each gate when you spot one and compare the minimum distance. 
    - This has a time complexity of O(m * n)
 - Or you can start from each gate simultaneously using a queue and then when a place is already visited, you'll know that the nearest gate already reached it. 
    - This requires a visited set.
    - This is also more efficient, as it's only O(m * n) as opposed to O(g * m * n).

 - Collect the starting points and put them into the queue and a visited set. 
 - Have a distance variable that increments per level of the queue. 
 - Write the bfs with while q, for _ in range(len(q)), pop left, set the room equal to distance (start with 0 so gates are set to 0), and then add the adjacent rooms to the room that you're on. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)