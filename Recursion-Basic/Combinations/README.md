# Leetcode 77 - Combinations (Medium)

**Topic**: Basic Recursion
**Link**: https://leetcode.com/problems/combinations/description/

## Notes:

# Recursion 
 - Create an array to store the answers. 
 - Create a recursive helper function. 
    - The point of this recursive function is to break this down into two choices: take the number or not. 
        - The first choice to be taken was to not take the current number we're on.
            - If that's the case, we continue that path by exploring its depth. 
            - The first base case we reach is what happens when it exceeds the range of 1 to n. 
            - If it does, we simply return. 
        - Then, we pop back one level to add n. 
            - When we do, we see that it doesn't even have length of k. However, that's taken care of because it'll eventually exceed n again when it makes the n + 1 recursive call (remember, we're on n). 
        - After we added n and finished the subsequent recursive call, we pop. 
            - There's an important edge case here where if k = 1, we need to check if len(arr) is equal to k before we check if i > n. 
    - Then we pop back until we reach a level where we can add k elements to the array. 
    - That's our next base case: if the length of the array that we're passing in between each function call is equal to k, there's no point adding more elements to the array. 
 - Outside of the helper function, simply call helper(1, empty array)
 - return the answer array. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(k * C(n, k)) -> This is because there are n * (n - 1) * (n - 2) choices. 
- Space: O(k * C(n, k)) -> for the answer output space. 
- Space: O(n) -> for extra space since the maximum depth you're recursing in O(n)

