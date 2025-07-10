# Leetcode 36 - Valid Sudoku (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/valid-sudoku/description/

## Notes: 
 - Formula is dividing rows by (floor division) and multiplying that result by 3, then adding that to columns // 3. 
    - subgrid_ind = j // 3 + (i // 3) * 3
 - Be mindful of the "." placeholder. They'll be added to the sets, causing False triggers if you don't ignore them. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(n)