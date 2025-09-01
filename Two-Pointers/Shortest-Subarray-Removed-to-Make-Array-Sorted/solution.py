class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while right >= 0:
            if right < len(arr) - 1 and arr[right + 1] < arr[right]:
                break
            right -= 1
        
        res = right + 1

        while left < right < len(arr):
            if left > 0 and arr[left] < arr[left - 1]:
                break
            
            while right + 1 < len(arr) and arr[left] > arr[right + 1]:
                right += 1

            res = min(res, right - left)
            left += 1

        return res