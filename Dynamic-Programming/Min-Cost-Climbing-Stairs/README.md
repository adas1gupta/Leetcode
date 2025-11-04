# Leetcode 746 - Min Cost Climbing Stairs (Easy)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/min-cost-climbing-stairs/

## Notes: 
 - Think of DP problems like decision trees. 
 - You can either make a decision to jump 1 step or 2 steps. 
 - You can also start from index 0 or 1. 

 - TOP DOWN DP:
 
 - The recurrence relationship is that you want to take the cost of the current element you're on and then the minimum of the (cost to jump 1 step, cost to jump 2 steps)
 - Base cases are if you exceed the array or if you're cached/memoized. 

 - Then, simply calculate the memoized value using the recurrence relation.

 - Finally, take the minimum of (dp(index 0), dp(index 1))

 - BOTTOM UP SPACE UNOPTIMIZED DP:
 
 - Since you can take either 1 or two steps, you'll have two extra items at the end of the array. 
 - Their values will be 0 because what you're trying to calculate is cost as it accumulates. 
    - As a result, you don't want to mess up the cost calculations.

 - BOTTOM UP SPACE OPTIMIZED DP:
 
 - You care about what the cost is at i + 1 and i + 2. 
    - It makes sense to take the minimum of the two, right?

 - Keep two variables to represent i + 1 and i + 2. 
    - The goal is to have them end up at i = 0 for the first start point and i = 1 for the second start point. 
 
 - As you start from the back to the front, you'll have the current cost, and you'll add the minimum of the two variables that are pointing to i + 1 and i + 2. 
 
 - Then, i + 1 will move to i. It should store the minimum cost that was calculated with current + min(i + 1, i + 2). 
    - And i + 2 will move to i + 1 to maintain the window size of 2. 
 
 - It's entirely possible that i + 2 will the minimum between the two, so then that will be used to calculate the minimum. 
    - i + 1 will move to the new minimum while i + 2 retains the old minimum. 
 
 - One of these two will be the minimum, so take the minimum of either accumulated values. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)