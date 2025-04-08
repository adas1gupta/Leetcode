# Leetcode 3483 - Unique 3-Digit Even Numbers (Medium)

**Topic**: Basic Recursion
**Link**: https://leetcode.com/problems/unique-3-digit-even-numbers/description/

## Notes:

# Recursion 
 - Since you're looking for unique numbers, you should use a set to account for uniqueness.  
 - The recursive helper function takes in two arguments:
    - A path to build out the different numbers. 
    - A list that keeps track of used digits. 
    - The recursive base case is when the length of the path array is 3 items. If it is, simply check if it's a valid number to add to the set. 
        - Make sure you add a return statement to the base case because it continues to the for loop and builds paths greater than three.
    - Then, you use a for loop through the used array. 
        - If the item you're currently on in the used array is True, that means the digit is already present. 
            - Since that's the case, just continue.
        - Otherwise, it's time to use the digit. 
            - Set the digit in the used array to be true. 
            - Append that digit to the path. 
            - Call the recursive helper function. 
            - The recursive helper function will build out the path array. 
            - Pop from the path array, and set the digit in the used array to be false because it's done being used for one of the digit iterations, but it can be used for later combinations.
    - How the recursive function acts is that it builds out the path until the path array is length two.
        - For example, in the array [1, 2, 3, 4], it'll put 1 in the path array and set it to be used. 
        - Then, it goes to the next function call, sees that 1 is used, and goes to the next number, which is 2. It adds 2 to the path array. 
        - Then, it calls the recursive function again and goes to 3, and then it calls on 4, and then the base case is reached. 
        - Then, it goes back to function call that was on used digit 3 and pops 3 from the array to go to 4. 
        - Then, it's done with the path of [1, 2, n], and goes to form paths with [1, 3, n]. 
        - Finally, after it's done with all the paths that can be formed with [1, m, n], it goes to [2, m, n] where 1 can be m or n. 
 - Finally, it just calls the helper function on an empty path list and a used digits array with all digits used status being set to False. 
 - The previous version of the helper function doesn't allow you to reuse digits from previous items in the array, so you're not generating all possible permutations
    - For example, in the array [1, 2, 3, 4], you reach 2, and you completely forget about forming numbers with the digit 1. 
 - Finally, return the length of the set. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n ^ 3) -> This is because there are n * (n - 1) * (n - 2) choices. 
- Space: O(n) -> maximum recursion depth is 3 so the only space complexity proportional to the size of the array is the used digits array. 