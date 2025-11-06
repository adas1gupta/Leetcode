# Leetcode 399 - Evaluate Division (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/evaluate-division/description/

## Notes: 
 - This is a weighted graph problem.
 - The edges are the result of a / b, which is computed for you already in the values array.
 - The problem provides queries, each of which ask what x / y will compute to.  
 - The key mathematical relationship to understand here is that if you want to calculate x / y, it's best to do it with x / z * z / y. 
    - Aka the edge between x and some value and some value and y. 

 - Build the adjacency list to store relationships between numberators and denominators. 
    - This is undirected. 
 - When you push to the adjacency list, push the (number, a / b (aka the weight)). 
    - b / a is 1 / (a / b). 
 
 - Create a dfs function that will take in the two query values. 
 - One of the base cases is that it's possible for a query to pass in a variable that doesn't even exist in the dictionary.
    - In that case, return -1. 
 - It's also possible that you're trying to divide a variable by itself.
    - This is in the case where you keep calling dfs(neighbor, second, visited) until you reach second.
    - You need a value to push back up. 
    - That value will be 1.
        - This is because a / b * b / c * c / d * d / d is essentially the same thing as a / d * 1, which is the same as a / d. 
    - Return 1

    - Furthermore, it's entirely possible that there is no path from a variable to itself. In that case, we want to return 1, but we end up returning -1.
    - This is why a base case is needed to check for that and it fits nicely with the a / d * d / d idea. 

 - Also, the reason why we can make repeated dfs calls is that a / b * b / c * c / d will have the variables beside a / d cancelled out. 
    - This is why dfs works here. 
 - Go through the neighbors and their weights.
    - First check if you're in a cycle so you don't end up infinitely recursing. 
 - Then, call dfs on neighbor and target/second. 
 - If you find a path (aka result != -1), return the weight you're on at the top of the stack (aka just weight) * the value propagated back up. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)