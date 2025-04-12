# Leetcode 56 - Merge Intevals (Medium)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/merge-intervals/description/

## Notes:
 - This time, you’re lacking a new interval to compare with. 
 - The algorithm here is that you are comparing the current interval you are on with the previous interval that’s in the result list. 
    - You check if the start time of the current is less than or equal to the end time of the previous.
    - If it is, change the end time of the previous to be equal to the maximum of the end time of the current one or the end time of the previous one. 
        - This is because there are edge cases where the previous interval added is actually the larger interval, and the current interval just happens to be a part of that larger interval. 
    - If it’s not, then those are separate intervals, and you simply append the current one. 
 - Then, return the result array. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(logn) -> binary search
- Space: O(logn) -> logn calls 