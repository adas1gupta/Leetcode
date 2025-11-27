# Leetcode 210 - Course Schedule 2 (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/course-schedule-ii/

## Notes: 
 - This is a topological sort problem since we're dependent on order in a graph (something must happen before something else)
 - Only time we return an empty array is when we have a cycle. 
 - Topological sort uses postorder dfs, so that means you add the node after you run dfs (preorder is before and inorder is only for binary trees)

 - Create the adjacency list. 
 
 - Have a set for determining if there's a cycle. 
 - Have a set for visited nodes to be more efficient and save time. 
 
 - In the dfs, return False for cycle and True for visited.
 - Add the current course to the cycle so that as you explore it and hit the course again, you know to return false.  
 - Go through the adjacency list for the course you're on and call dfs. 
 - After you pop back to the current course from the dfs, remove the current course from the cycle set, add it to the visited set to save work, and then add the current_course to the output list. 
 - 0 -> 1 -> 2 -> 3 -> 4 leads to a list of [4, 3, 2, 1, 0] since it's postorder. 

 - If you ever encounter a False from the dfs, return a False within the dfs and an empty array in the outer function. 

 - Okay, the way you actually do Topological Sorting is:
   - build an adjacency list. 
   - create UNVISITED, VISITING, VISITED constants
   - create a state array that's initialized to UNVISITED (state = [UNVISITED] * numCourses)
   - proceed as normal


## Mistakes:
 - If you try to not use a visited set, you end up checking if adjacency_list[course] == [].
    - This poses a problem because in the base case check, you have to append the item before you return True, but you risk appending the same item multiple times. 
 
 - Since that's the case, it's best to just use a visited set. 

 - Use two sets to detect cycle and not perform topological sort + add items multiple times to the result list
 - Make sure that when you reach the base course (no prereqs), you add that course to the visited set so that you don't add it multiple times to the result set. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)