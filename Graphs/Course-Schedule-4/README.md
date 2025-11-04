# Leetcode 1462 - Course Schedule 4 (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/course-schedule-iv/description/

## Notes: 
 - Create the adjacency list. 
 
 - Have a hashmap to store the indirect and direct prerequisites of every node. 
 - The key will be the node, but the value should be a set of indirect and direct nodes. 
 - It's also important the hashmap remain empty. Makes it easier to check if it has already been populated. 

 
 - In the dfs, check if there is a set of indirect and direct prereqs. 
    - If there is, simply return it. 
 - If not, initialize a set, go through the direct prereqs of the current node. 
    - Keep in mind that what you will retrieve is a set of indirect and direct prereqs from the prereq of the current set. 
    - Go through that set, and add it to the set of the current node. 
 
 - Important to also add the direct prereqs to the set of the current node because:
    - Let's say you have nodes 2, 1, and 0. You end up at node 0, and its set will be empty because it has no indirect prereqs. 
    - Node 1 goes through the set of node 0, and that set will be empty, so set of Node 1 is also empty. 
        - This is fine because node 1 also doesn't have any indirect prereqs. 
    - However, when we reach node 2, it will receive an empty set from node 1, and then node 2's set will also be empty.
        - This is wrong because node 2 has an indirect prereq of node 0. 
 
 - Call dfs on each course. 
 - Go through the queries and simply check if left is in the hashmap containing node to indirect and direct prereqs. 
 - Append them to the result list. 

 - TIME & SPACE COMPLEXITY

 - Adjacency list is O(E) time. 
 - You go through 

 - Adjacency list is V + E space because you are storing V courses and then the lists are storing E relationships. 



## Mistakes:
 - Make sure to actually add the direct prereq of the node to the current_node because the prereqs of the prereq are the indirect node you want to add. 

 - Remember that the TIME complexity for dfs is O(V + E) because:
    - Let's say you have nodes 1, 2, and 3, and they each have 3 edges. 
    - When you dfs, you go through v nodes and 3 edges for each node. 
    - That means you went through 9 edges and 3 nodes, which coincides with V + E. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)