# Leetcode 70 - Climbing Stairs (Easy)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/climbing-stairs/description/

## Notes: 
 - Think of DP problems like decision trees. 
 - You can either make a decision to jump 1 step or 2 steps. 

 - Once we reach n or exceed n is when we stop the buildout of the tree.
    - This builds our base cases. 
        - If dp(i) > n: return 0, but if dp(i) == n, return 1. 

 - What we also notice is that when we build out the tree, there are repeated nodes. 
    - Given that, we can use memoization (memo = {}) to store these nodes. 
    
    - Also, introduce the base case of if dp(i) is already stored in the memo hashmap, just return its value. 
    - If not, simply calculate memo[i] to be the recurrence relationship. 
    - Then, return it at the end. 
 
 - Call dp(0) to build from 0 to n. 

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