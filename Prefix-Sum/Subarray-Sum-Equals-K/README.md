# Leetcode 560 - Subarray Sum Equals K (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/subarray-sum-equals-k/description/

## Notes: 
 - Just think of this problem as a prefix sum problem where you're trying to understand what prefix you can chop off. 
 
 - Also have to include 0 in case the prefix sum equals to k.

 - Also, have to check before you update the prefix_sum in the hashmap.
 - If you do it after the hashmap update, you're effectively saying that you can chop off the entire array, including the element you're on, and an empty array would be valid, which is not the case. 

 - Sliding window doesn't work here because we need the order to be maintained and negative numbers affect calculations.
 - For example, if the target were to be 5, and we are on sum 7, it's possible that we'll encounter a -2 down the line, leading to the sum being 5 and a valid array being found.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)