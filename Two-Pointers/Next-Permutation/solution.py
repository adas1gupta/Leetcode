class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap, to_swap = len(nums) - 1, len(nums) - 1

        while swap >= 0:
            if swap < len(nums) - 1 and nums[swap] < nums[swap + 1]:
                break
            swap -= 1

        while to_swap >= 0:
            if nums[to_swap] > nums[swap]:
                break
            to_swap -= 1

        if swap != -1:
            nums[swap], nums[to_swap] = nums[to_swap], nums[swap]

        left, right = swap + 1, len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1