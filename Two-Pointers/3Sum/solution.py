class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s, m, e = nums[i], nums[j], nums[k]
                if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                if s + m + e > 0:
                    k -= 1
                elif s + m + e < 0:
                    j += 1
                else:
                    solution.append((s, m, e))
                    j += 1
                    k -= 1
        
        return solution