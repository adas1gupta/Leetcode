# Leetcode 261 - Graph Valid Tree (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/graph-valid-tree/

## Notes: 
 - Adjacency_list, but slightly adjusted since it's undirected (both nodes are added to each other's list)

 - The two criteria for a graph not being a tree is if there's a cycle and if there are disconnects in a graph (more than 1 graph)

 - Have a visited set to check for a cycle. 
 
 - The dfs needs to take in the previous node as an argument because nodes that are connected will be a part of each other's lists, so that will incorrectly lead to a cycle existing. 
 - Check if there's a cycle for the base case and return False if so. 
 - Add the node to the visited/cycle set. 
 - Go through the neighbors and check if you receive a false value. 
    - Make sure the neighbor isn't the same as the previous node. 
 - Afterwards, return True. 
 - The reason why we return True is so that when we check if the dfs call in the outer function yields a False (because there's a cycle), there is a way for us to tell that there was no cycle.
 
 - Don't simply call dfs in the outer function. Call a dfs and check the result to see if a cycle was yielded.
    - 0 -> 1 -> 2 -> 3 -> ... and so on -> 0. There's n nodes and we record all of them, but there was a cycle. 
    - Choose -1 as the previous because we don't use or do anything with previous except for a simple comparison, so you can choose whatever value that you want as long as it can't be one of the possible values for a node. 
        - Can choose -1 or n + 1
 
 - Then, to check for more than 1 graph, simply check if the length of the visited set is equal to the number of vertices. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)