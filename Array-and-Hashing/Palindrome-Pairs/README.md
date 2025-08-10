# Leetcode 336 - Palindrome Pairs (Hard)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/palindrome-pairs/description/

## Notes: 
 - key insight is that you want to go to each word and see what is missing from a word to make it a palindrome.
 - Basically, if you use lls as an example, "s" is something you can use, so is "ll", so is "lls", and "sl", and so on. 
 - This basically requires you to break down each word into a combination of two parts (looping through each word). 
 - Then, checking if the reverse of either part exists and if the other corresponding part is already a palindrome yields the other word that can be combined with the original word to form a palindrome. 
 - When you find something that works, simply make sure that it isn't the word that you're currently on. 
 - The reason why you need a set to prevent duplicates is that when you encounter full words that are palindromes of each other,
 they are being counted twice because of the if and if instead of if and elif. 
    - 'abcd' counts 'dcbaabcd' at the beginning and 'abcddcba' at the end of its iteration. 
    - Then, it repeats for 'dcba'. 
    - You need the if and if because you want to check:
        - second_half_reversed + palindrome_first_half + second_half
        - first_half + palindrome_second_half + first_half_reversed
        
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)