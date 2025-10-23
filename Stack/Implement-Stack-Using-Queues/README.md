# Leetcode 150 - Evaluate Reverse Polish Notation (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## Notes: 
 - For O(n) push, append first, pop and append elements except for the last element in the deque, and only return the first element for the top method. 
 - If you do self.stack[-1], it returns the last item in the queue. 
 - Same for O(n) pop. Just pop and append until the last element, then pop the last element. 
 
 - The algorithm for this is to simply pop from the queue until you reach the last element. Thus, the last element is always first for either push or pop. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string