class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = {}
        to_return = 0

        for num in nums:
            digit_sum = 0 
            for char in str(num):
                digit_sum += int(char)
            
            if digit_sum in digit_sums:
                to_return = max(to_return, num + digit_sums[digit_sum])
                digit_sums[digit_sum] = max(num, digit_sums[digit_sum])
            else:
                digit_sums[digit_sum] = num
        
        return to_return if to_return != 0 else -1