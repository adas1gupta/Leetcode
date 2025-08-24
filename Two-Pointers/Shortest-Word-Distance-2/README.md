# Leetcode 244 - Shortest Word Distance II (Medium)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/shortest-word-distance-ii/description/

## Notes: 
 - You can do better than O(n)
 - Use preprocessing to store the indices of words in self.word_arr.
 - Then, use the linked list pointer increment pattern to go through the indices of the first and second words to find the smallest distance. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string