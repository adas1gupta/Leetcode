# Leetcode 42 - Trapping Rain Water (Hard)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/trapping-rain-water/description/

## Notes: 
 - [3, 0, 1, 2, 5]. This is the test case where the maximums are already at the beginning and end. If we process in any order, it will not matter. 
 - [3, 0, 5, 2, 4]. This test case is where the maximum appears earlier than the end. If that's the case, then elements before the maximum don't matter because their minimum always remains 3. 
    - However, we would want to process the elements after we discover the next maximum because that's when the current maximum becomes the next largest minimum of the maximums. 
    - For example, 2's minimum is 4, not 3. 
    - This implies that we want to find the next maximum asap.
 - [3, 0, 4, 2, 6]. This test case is where there's a new largest minimum. Elements before the next largest minimum are processed the same, but the elements after the next largest minimum aren't.
    - This is basically the same idea as the test case above it where we want to process the elements before we find the next largest minimum of the maximums.  
 - What about test cases where the minimum is from the right? 
 - [4, 0, 1, 2, 3]. It seems like we can process in whatever order. 
 - [4, 0, 5, 2, 3]. It seems like we need to process from right to left. Seems like we need to process elements starting from the next largest minimum, which in this case is 3. 
 - [5, 0, 6, 2, 4, 1, 3]. The pairs of maximums are (3, 5), (4, 6), (5, 6). 
    - We want to process from 3 to 4 first. 
        - That means we start from 3. 
    - It seems like the maximum doesn't matter. 
        - It's only the minimum matters. 
    - Then, we'll eventually reach 5 and 6, and we start processing from 5. 
 - So it seems like we process the smaller elements and don't care about the maximum. 
 - We just want to find the next largest minimum of the maximums. 
 - We have to anchor the actual maximum in case we find an element that's larger than the current maximum. 
 
 - This is why we keep track of the maximums from the endpoints. 
 - We calculate the maximums from both sides to determine which one is smaller. 
 - The formula is min(left_max, right_max) - min(height[left], height[right]) because we only care about the minimum of the maximums and we want to process the smallest elements before we find the next minimum of the maximums. 
 - We want to process the smallest elements so that when we've found the next minimum of the maximums, we can use that new minimum to calculate the rainwater. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string