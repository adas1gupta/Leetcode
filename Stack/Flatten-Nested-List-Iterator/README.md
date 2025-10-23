# Leetcode 341 - Flatten Nested List Iterator (Medium)

**Topic**: Stack
**Link**: https://leetcode.com/problems/flatten-nested-list-iterator/description/

## Notes: 
 - Don't try and break down the Nested List into an actual list. 
 - Don't try to continually reverse in the first try. 
 - Think about lazily processing. 
 - Look at this test case:
 - [-3, -4, [-5, [-6, -7]]]
 - The [::-1] turns this into [[-5, [-6, -7]], -4, -3]. Notice how the inner list isn't reversed.
 - Then, we approach the Nested List, and when we reverse it, we get it [[[-6, -7], -5]]. Notice the pattern of how, level by level, the list is eventually reversed to the order that we want it in. 
 - This is why we don't need to continually reverse in the first try. 
 - Remember to use the while condition while self.stack

 - Use a stack initialized with all elements in reverse order.
 - In hasNext(): While the stack's top is a list (not an integer), pop it and push its contents onto the stack in reverse order. Return true if an integer is found at the top, false if stack is empty.
 - In next(): Pop and return the top integer (hasNext() guarantees it's an integer).
 - The key insight is that hasNext() does the flattening work lazily by unpacking nested lists only when needed.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string