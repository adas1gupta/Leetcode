# Leetcode 716 - Max Stack (Hard)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/max-stack/description/

## Notes: 
 - You'll need a max_heap and a stack. 
 - However, the dilemma arises when you pop from stack, but the element you pop is in the middle of the max heap. 
 - The way around that is tagging a unique ID to each element and using a set to keep track of what unique IDs have been removed. 
 - The one edge case that you need to worry about is what happens when multiple of the same element gets added. 
 - The reason why this is an edge case is that when you add multiple of the same element to the max_heap, you want to remove the elements with the most recent unique IDs. 
 - This is because when you remove the wrong duplicate and then check for peekMax or top, you need to pop off the elements with the removed Id and removing the wrong ID doesn't remove those elements.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string