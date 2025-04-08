import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def helper(i, arr):
            if len(arr) == k:
                ans.append(copy.copy(arr))
                return
            elif i > n:
                return
            helper(i + 1, arr)
            arr.append(i)
            helper(i + 1, arr)
            arr.pop()
        
        helper(1, [])
        return ans
