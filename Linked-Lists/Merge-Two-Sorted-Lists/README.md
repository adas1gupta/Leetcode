# Leetcode 21 - Merge Two Sorted Lists (Easy)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/merge-two-sorted-lists/description/

## Notes: 
 - Use the dummy pattern here. 
 - Create a dummy node and then a crsr that starts at the dummy node. 
    - This crsr will link from node to node.

 - Then, have pointers for the first and second list. 
 - The idea is that you'll see which node is smaller, link crsr to it, then move forward the smaller pointer between first and second. 
 
 - The key edge case you have to keep in mind is that you don't want to link first to second and second to first.
 - You don't know how many nodes in the first list are smaller than the current node you're on in the second list and vice versa.
 - So linking the smaller node to second and then moving first while the next first could also be less than second is wrong.
 - 1 -> 2 -> 3, 3 -> 4 -> 5 would lead to 1 -> 3 -> 3 -> 4 -> 5 
                                          2 -> ^

 - Then, simply check which pointer finished earlier between first and second and link crsr to the one who finished later. 

 - Finally, return dummy.next

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 