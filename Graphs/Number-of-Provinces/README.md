# Leetcode 547 - Number of Provinces (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/number-of-provinces/description/

## Notes: 
 - Use Union-Find because the problem is asking you to find groups. 
 
 - To implement Union Find, these steps are required. 

 1. Initialize a parents array with each value being equal to index (parents = [i for i in range(n)])
 2. Initialize a ranks array with each value being 1. 
    a. The point of the ranks array is for an optimization where the smaller graph is attached to the bigger one. 
 3. Create a find function that checks while the number is not equal to its index in the parent array. This find function is for finding owners of groups.  
    a. Set the index equal to whatever value parents[num] is pointing at (parents[num] = parents[parents[num]])
    b. Set num equal to parents[num] to perform the comparison again for the while loop. 
 4. Create a union function to compare which owner has a larger rank to see which owner swallows the other. 
    a. Find the owners of the two numbers. 
    b. If they have the same owner, just exit. 
    c. If the other owner is larger, set the parents[smaller_owner] = parents[one]
    d. Add the rank of the smaller owner to the larger owner. 
 
 5. Since this is an adjacency matrix, just loop through and see which (i, j) == 1, and call union on that (i, j)

## Mistakes: 
 - Don't try and count the number of unique parents using len(set(parents)). 
   - This is because you might union 1 and 2 and then union 2 and 3 but 1 isn't unioned to 3, so there will be an overcounting of provinces. 
 - Simply count how many items are equal to its index in the parents array. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)