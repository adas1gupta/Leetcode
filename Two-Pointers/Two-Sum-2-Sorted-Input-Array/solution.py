class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            start = numbers[l]
            end = numbers[r]

            if start + end > target:
                r -= 1
            elif start + end < target:
                l += 1
            else:
                return [l + 1, r + 1]