# Leetcode 30 - Substring with Concatenation of All Words (Hard)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

## Notes: 
 - First thing to clarify here, this is not an anagram or a permutation of characters problem. This is a permutation of WORDS problem. 
 - Here is an example to clarify:
    - ["ab","cd","ef"]: ["abcdef", "abefcd", "cdabef", "cdefab", "efabcd", "efcdab"]. 
    - First, you find permutations of each individual word and then add them together. 
    - The key difference is that examples like this don't count because there is no permutation of 'ab' that leads to 'ac': acdbef
 
 - Another key thing to note here is that multiple copies of a word is allowed. 
    - This creates the need for a dictionary to store the word and its frequency in O(1) time. 
 - Another key thing is that all the words are the same length
 - The algorithm will be a fixed size window where we break the window into pieces that are the same length as each of the words in the input. 
 - Then, we'll decrement the frequency of the left word and increment the frequency of the right word. 
 - We'll utilize the number of matches algorithm here. 
 
 - When utilizing the two pass number of matches algorithm, it's important to note that we don't need to increment right after the first pass. 
 - This is because right is already on the next word. 
 - Here is the example I'll refer to:
    - s = "barfoothefoobarman"
      words = ["foo","bar"]
      word_len = 3, window_size = 6
    - For offset of 0:
        - left = 0, anchor = 0, right = 6
          s = "b a r f o o thefoobarman"
               0 1 2 3 4 5 6
               ^           ^
              left       right
        - As you can see, right points to 6, which is the word the instead of foo. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string