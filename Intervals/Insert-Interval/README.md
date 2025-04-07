# Leetcode 57 - Insert Interval (Medium)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/insert-interval/description/

## Notes: 
 - Given a list of intervals and an interval to add, make sure there are no overlapping intervals. 
    - When your list has [1, 3], and you add [2, 5], make sure the intervals merge to become [1, 5]. 
 - You can assume that they are sorted based on their start times. 
 - [1, 2] and [2, 3] count as an overlap. 
 - Okay, the reason why you use extra space here is because of the manual shifting that you need to do and the fact that an overlapping interval can take multiple intervals. 
 - Create a result list to store the new intervals. 
 - Create a start pointer. 
    - The start pointer will initially add items to the result list that have intervals whose end time is less than the start time of the interval to be added. 
    - Then, it will go through the intervals whose end time is greater than or equal to the start time of the interval to be added and whose start time is less than or equal to the end time of the interval to be added. 
        - Interval[i][1] >= newInterval[0] and interval[i][0] <= newInterval[i][1]
        - This is because when you visualize newInterval as a number line, it’ll extend until it reaches or surpasses one of the interval’s start times. 
        - It will also start before an interval’s end time or at another interval’s start time. 
    - Then, it will go through the rest of the intervals and add them as long as their start time is greater than the end time of the interval to be added. 
 - Then return the result. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 