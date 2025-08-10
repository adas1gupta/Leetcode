# Leetcode 381 - Insert Delete GetRandom O(1) - Duplicates allowed (Hard)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

## Notes: 
 - Think back to the Amazon interview. 
    - Grab a random number by using the range of the array boundaries (start - 0 && end - len(arr) - 1)
    - Then, use that random number to grab a random item from the array in O(1) time (self.arr[random_number])
    - If you want to remove items quickly from an array, swap what you want to remove to the end and pop (O(1) time)
 - Then, have the map store a list of indices that correspond to where a number and its duplicates are held in the array. 
 - This way, you can quickly check if a number is already present in the array in O(1) time. 
 - Don't make the mistake of comparing if the value you're removing is equal to the value at the end of the array. 
    - Rather, what you care about is if the index you're trying to remove is the last index in the array. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)