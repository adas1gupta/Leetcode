class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = { 0: 1 } # if the running_sum is exactly equal to k 
        running_sum = 0
        total = 0

        for num in nums:
            running_sum += num

            diff = running_sum - k
            if diff in prefix_sums:
                total += prefix_sums[diff]

            prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1
            
        return total