class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = float('inf')
        to_return = 0

        for i in range(len(nums) - 2):
            num = nums[i]
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                first = nums[i]
                second = nums[j]
                third = nums[k]
                
                triplet_sum = first + second + third
                diff = abs(target - triplet_sum)
                if diff == 0:
                    return triplet_sum
                elif diff < closest:
                    closest = diff
                    to_return = triplet_sum
                
                if triplet_sum > target:
                    k -= 1
                else:
                    j += 1
                

        return to_return
