# Leetcode 739 - Daily Temperatures (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/daily-temperatures/description/

## Notes: 
 - Utilize a monotonic decreasing stack. 
 - A monotonic stack is strictly decreasing. 

 - Keep a result list and a stack. 

 - Basically, you append a value. 
    - If the next value is greater than the previous, then pop it off the stack and update the index of the result list that you popped off with the current number you're on MINUS the index you popped off. 
 - If it's not, then append it.
 - That's because we want to update that index too. 
    - Now, you're wondering: How do you update the temperatures at the back? 
        - You simply use a while loop and keep continuing until there's nothing left in the stack. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 