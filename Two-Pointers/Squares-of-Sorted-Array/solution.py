class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        start, end = 0, len(nums) - 1
        ptr = len(res) - 1

        while start <= end:
            left, right = nums[start], nums[end]

            if left ** 2 >= right ** 2:
                res[ptr] = left ** 2
                ptr -= 1
                start += 1
            else:
                res[ptr] = right ** 2
                ptr -= 1
                end -= 1
        
        return res
