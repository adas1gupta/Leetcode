# Leetcode 690 - Employee Importance (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/employee-importance/description/

## Notes:
 - The input is a bit hard to understand.
 - Essentially, it's just Employee objects.
 - Just go through each Employee and map ID to Employee.
    - Reason is that we are starting with ID and want to bounce from ID to ID.
    - Thus, we need a way to access ID in O(1) time.

 - No need for a visited set because subordinates implies that you cannot have a manager be a subordinate to an employee.


## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 