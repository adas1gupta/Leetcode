# Leetcode 895 - Maximum Frequency Stack (Hard)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/maximum-frequency-stack/description/

## Notes: 
 - Store the actual frequency of each element pushed so that we know what the previous frequency of any new element being pushed is. 
 - Create a frequency map where you have a frequency as the key and list of elements at that frequency as a value. 
 - Create a variable to store the maximum frequency. 
 
 - Get the frequency of the element being pushed. 
 - Record the max_frequency. 
 - Then, see if the frequency that you collected for the current element is in the frequency_map, and if it's not, initialize and empty list.
    - The reason why there's no need to update the previous frequency's list is that when the max_frequency element is popped, it'll be 1 less, so the previous_frequency will have that element in the list.  
 - Append the element being pushed to the frequency's list in the frequency_map. 
 
 - Pop the max_frequency's list in the frequency map. 
 - Then, update the frequency of the element that was popped in the first map. 
 - Then, check if the max_frequency's list in the frequency map is empty. 
    - If it is, decrement max_frequency by 1.
    - The reason why we do this is because the next max_frequency is naturally going to be max_frequency - 1 because if the max_frequency of the element was 6, and then we pop, the element that was most frequent will now have a frequency of 5. 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string