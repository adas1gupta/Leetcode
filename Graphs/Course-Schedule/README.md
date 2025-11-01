# Leetcode 207 - Course Schedule (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/course-schedule/description/

## Notes: 
 - Essentially, we build relationships of what courses lead to what courses using an adjacency list where we store the result course as the key and the source course(s) in a list as the value.
 - Then, we go through the source courses and explore the path for each (implying dfs), adding them as we go.

 - The two conditions to trigger a base case are:
    - If the course that you're exploring has an empty list, implying that exploration is done and no course leads to a cycle.
    - The other condition is if the course path that you're exploring has a course that's already in the set, implying that there is a cycle somewhere since you came back to a point that you explored.

 - After you explore each source course using the for loop, you set the course in the adjacency list to an empty list to make it more efficient for checking for cycles.

 - Then just loop through the courses in the outer loop and run that dfs on it, seeing if you get a False at any point.


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)