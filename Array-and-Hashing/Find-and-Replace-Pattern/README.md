# Leetcode 890 - Find and Replace Pattern (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/find-and-replace-pattern/description/

## Notes: 
 - The pattern needs to follow the order too, which makes the solution a little more complex. 
 - If order didn't matter, you could simply count the number of unique characters and then compare length. 
 - This means you pair letters together. 
    - Have one dictionary map one to another and another dictionary map another to the one. 
    - If they don't match or one of them is not in the dictionary while the other is, then that word is False -> break. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)