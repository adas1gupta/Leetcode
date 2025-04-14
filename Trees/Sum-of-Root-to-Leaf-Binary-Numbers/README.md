# Leetcode 1022 - Sum of Root To Leaf Binary Numbers (Easy)

**Topic**: Tree
**Link**: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

## Notes: 
 - have a total variable
 - have a helper recursive function that takes in the node and path variable
    - use the typical structure associated with leaf node questions.
        - if not node, return.
        - Some sort of code: in this case, adding the node.val to the path string. 
        - checking if it's a leaf node, and if it is, add to the total and return. 
            - total += int(path, 2) -> 2 indicates that the path string is a binary number, and int turns the binary number into base 10. 
        - bin(decimal_number) is the way to turn a decimal number into binary. 
        - Then, figure out when to call helper, and in this case, you can call helper on both freely because of the if not node taking care of the cases where the binary tree isn't complete.
 - Call the helper on the root and an empty string.
 - Return the total. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n * h) -> explore all the nodes multiplied by O(h) to convert the strings into numbers to add. 
- Space: O(h) -> height of the tree is the amount of space stored for the call stack


