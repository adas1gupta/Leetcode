class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = None
        difference = float('inf')

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                first, second, third = nums[i], nums[j], nums[k]
                three_sum = first + second + third
                diff = abs(target - three_sum)

                if diff < difference:
                    difference = diff
                    closest = three_sum

                elif three_sum < target:
                    j += 1
                else:
                    k -= 1

        return closest