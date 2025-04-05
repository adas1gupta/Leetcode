# Leetcode 703 - Max Area of Islands (Easy)

**Topic**: Heaps
**Link**: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

## Notes: 
 - The goal is to find the kth largest element in a collection even as elements continue to be added. 
 - You use a min heap because a min heap stores the k largest elements seen so far and min heap[0] will be equal to kth largest. 
    - This is because the top stores the smallest of the k largest elements.
    - To push or pop an element, it’s O(log n) time.
        - heapq.heappush(list, val)
        - heapq.heappop(list)
    - To build a heap from a list, it’s O(n). 
        - heapq.heapify(list) -> the list itself is now a heap
    - To peek the top item, it’s O(1):
        - list[0]
 - A max heap stores the k smallest elements where max heap[0] = kth smallest
    - This is because the top stores the largest of the k smallest elements.
 - Simply create a copy of the input list, heapq.heapify it, and when performing the add operation:
    - Add it. 
    - Keep popping from the minHeap until the length is equal to self.k.
        - There’s one edge case where the initial list doesn’t match size k, so only pop if the length of the minHeap exceeds k. 
    - Return the top of the element because you acquired the k largest elements and want the kth largest one (aka the smallest of those largest elements).
    - Remember, you want the kth largest element, not the kth smallest one. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(mlogk) #m is the number of calls; k is the size of the heap
- Space: O(k)