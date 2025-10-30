# Leetcode 997 - Find the Town Judge (Easy)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/find-the-town-judge/description/

## Notes: 
 - Create two hashmaps, one for how many people each person trusts and one for how many people trust each person.
 
 - Afterwards, loop through the array and record. 
 
 - Then check which person is trusted by the total number of people - 1 and if that person doesn't exist in the hashmap for how many people each person trusts. 

 - Then, return -1. 
    - However, there is one edge case where there is 1 person and nothing in the input array. 
    - If that's the case, you return 1 because one person that doesn't trust himself fulfills the conditions.  

 - This is O(V + E) time complexity because each item in the input array is an edge (edges correspond to the number of relationships that exist). 
 - Then, you loop through people, and V is the number of nodes (the nodes here are people)

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)