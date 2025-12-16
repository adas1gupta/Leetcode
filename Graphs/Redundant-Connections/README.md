# Leetcode 684 - Redundant Connection (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/redundant-connection/description/

## Notes: 
 - Undirected -> If you need to find distinct groups or detect a cycle -> UNION FIND
 
 - The reason why Union Find has the ability to detect edges is that the rank of each component in the connected graph will be the same. 
    - So if you try to connect them again, it's a cycle because one of the nodes is going back to a previous node that will lead back to the node ahead. 
    - (Draw it out if need be). 
    - So just check if both nodes have the same parent, and if they do, that's a cyclic edge. 

 - Reason why union find works here is because when you are trying to connect already connected components, you'll find that they have the same parent.
 - This means that if they're already connected, and you're trying to connect them, then there's a cycle.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)