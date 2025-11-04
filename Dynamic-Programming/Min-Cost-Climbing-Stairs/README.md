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
 
 - Build out the tree and cross out redundant portions until you can compress the tree into a line. 
 - This line is [curr = prev_one + prev_two, prev_one = prev_two + prev_three, ..., arr[n - 1] = arr[n] + arr[n + 1]]
 - This line means creating an array that computes position i from position i + 1 and i + 2.
   - So n - 1 will need n, which is 1, and n + 1, which is 0 (an overshoot)

 - BOTTOM UP SPACE OPTIMIZED DP:
 
 - Notice from above that all you care about is the previous and previous to previous elements. 
 - [next_elem to compute, n, n + 1]
 - [n = n + n + 1, n + 1 = n, who cares about this element]
 - Therefore, we only need two variables: prev, prev_prev where prev, prev_prev = prev + prev_prev, prev

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)