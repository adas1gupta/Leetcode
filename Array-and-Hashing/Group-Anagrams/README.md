# Leetcode 49 - Group Anagrams (Medium)

**Topic**: Array, HashMap  
**Link**: https://leetcode.com/problems/group-anagrams/description/

## Notes: 
 - The key takeaway from this problem is that you want to use a hashmap that stores the frequency of characters as keys, and the list of those items that match that frequency as values. 
 - However, dictionary keys must be immutable. As a result, if you are trying to use a dictionary, list, or set as keys, that does not work. 
 - Big takeaways from this problem are that you can use collections as keys or ways of uniquely grouping things + you can use tuples to turn them into keys. 
    - tuple(char_list)
    - In this problem specifically, you want to tuple on a char list because tuple on a dictionary will merely keep its keys instead of key values. 
 - Keep a hashmap to match character frequencies to matching strings. 
 - Loop through the strings, form a char_list for each string, and keep track of the counts of each character in the string. 
    - Simply create a list of size 26, and find the appropriate index using ord(char) - ord(‘a’). 
 - Then, tuple the char_list and put it into the dictionary.
 - Afterwards, return the values of the dictionary as a list
    - list(dict.values())

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(n)
