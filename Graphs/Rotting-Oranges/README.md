# Leetcode 286 - Walls and Gates (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/walls-and-gates/description/

## Notes: 
 - First thing that should immediately occur to you is that this problem is multi-source. 
 - Start from rotten oranges, collect them, and put them into a set and a queue. 
 - Also collect the fresh fruit so you know when to stop and create a fresh_to_rotten variable so you know how much you need until you can stop. 
 
 - Create the inner function to traverse where you check if you're out of bounds, visited already, or fresh_fruit equals fresh_to_rotten. 
 - Once you do that, add the cell you checked to the queue and visited set. 
 - If you see a fresh_fruit, increment fresh_to_rotten and add the fresh_fruit to the queue. 

 - Then, create a minutes variable, implement bfs, and keep incrementing. 
 
 - Last thing is to check for three conditions. 
    - If fresh is not equal to fresh_to_rotten, return -1. That means not all fresh fruit were able to rot. 
    - If fresh_fruit is 0, then the answer is actually 0 instead of -1. 
    - Otherwise we return minutes - 1. 
        - The reason why we do minutes - 1 is because when we finally turn fresh_to_rotten equal to fresh_fruit, we will perform a check on the last fresh fruit to turn rotten. 
        - Then, minutes gets incremented by 1 more than necessary. 



## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)