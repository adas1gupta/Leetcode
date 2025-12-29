# Leetcode 973 - K Closest Points to Origin (Medium)

**Topic**: Heaps
**Link**: https://leetcode.com/problems/k-closest-points-to-origin/description/

## Notes: 
 - Find the k closest points to the origin, which means that to collect the closest/smallest points, you use a maxHeap. 
 - Make a max_heap. 
    - A list works here just fine because heaps are lists. 
    - max_heap = []
 - Loop through the points, calculate their distance, and push to the maxHeap. 
    - Make sure to also include the coordinates because you want to associate the distance with the actual coordinates as well. 
    - heapq.heappush(max_heap, (-distance, x, y))
    - If the size of the max_heap ever exceeds k, just pop from it. 
 - Return a list of the x, y coordinates in the heap by simply looping through the max_heap and forming a list out of the item’s first and second indexes to add to the result list. 
 - Time complexity is n log k because the size of the heap is k, and heap operations are always log (size_of_the_heap), and those heap operations are happening every iteration of the for loop. 

## Mistakes:
 - Need to actually use x^2 + y^2 because using simple Manhattan distance leads to edge cases of equal Manhattan distance but unequal distance ((1, 3) vs (2, 2) aka 10 vs 8)

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(nlogk) #n is the length of the input array; k is the size of the heap
- Space: O(k)