# Leetcode 2364. Count Number of Bad Pairs (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/count-number-of-bad-pairs/description/

## Notes: 
 - The brute force is obvious.
 - Figure out what information you can gather at each element. 
    - In this case, the formula for a good pair was j - i = nums[j] - nums[i]
    - This formula would require two elements, but instead, rearrange this to be j - nums[j] = i - nums[i] 
 - If i - nums[i] appears again as you are going through the array, that means there exists an element where the formula suffices. 
 - That means you would want to store i - nums[i] along with the frequency of its occurrence. 
 - Afterwards, you will realize that the number of good pairs you can form is the (frequency * (frequency - 1) // 2). 
 - Then, to find the bad pairs, collect the number of good pairs and subtract it from the number of pairs possible. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)