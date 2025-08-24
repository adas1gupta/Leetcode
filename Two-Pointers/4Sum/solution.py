class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        nums = sorted(nums)
        print(nums)

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                k, l = j + 1, len(nums) - 1

                while k < l:
                    first = nums[i]
                    second = nums[j]
                    third = nums[k]
                    fourth = nums[l]
                    quad_sum = first + second + third + fourth

                    if quad_sum == target:
                        quadruplets.append([first, second, third, fourth])
                        
                        while k < l and nums[k] == third:
                            k += 1
                        while l > k and nums[l] == fourth:
                            l -= 1
                    
                    elif quad_sum < target:
                        while k < l and nums[k] == third:
                            k += 1
                    else:
                        while l > k and nums[l] == fourth:
                            l -= 1

        return quadruplets 