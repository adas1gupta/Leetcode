# Leetcode 133 - Clone Graph (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/clone-graph/description/

## Notes: 
 - The input is a reference to a node in a connected undirected graph. 
 - The goal is to create a deep copy of the graph
 - There are node objects that have:
    - Fields:
        - Val
        - Neighbors array
    - Constructor:
        - Default value for val is 0
        - Default value for neighbors is None
 - First, have a hashmap mapping the input nodes to the corresponding clones. 
    - Reason why you have this is so that when you spot the node in the graph you're building out, you know which copy to immediately grab. 
 - Use a graph traversal algorithm like dfs. 
    - Take in a node because that’s what you’re selecting to iterate past. 
    - The base case is that if a node already exists, then it’s cloned, so return its clone. 
    - Create a clone of the node that you’re on and enter it into the hashmap. 
    - Go through the neighbors of the node you’re currently on, and append it to the clone’s neighbors field. 
        - What you append is the result of the dfs call on the neighbor node you’re currently on in your iteration journey. 
    - Return the copy as that will be the answer/head of the new graph. 
 - return dfs(node) if node is not null and if it is, return None

 - Algorithm is basically knowing which copy to grab based on the original node by using a dictionary -> using dfs to traverse the graph -> create a copy of the node using Node(node.val) -> storing the copy in the dictionary -> going through the neighbors of the original and appending the copy of the neighbors (using dfs call) to the neighbors array for the copy. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)