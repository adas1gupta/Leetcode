class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        longest = 0

        for num in elems:
            if num - 1 not in elems:
                curr = num
                while curr in elems:
                    curr += 1
                
                longest = max(longest, curr - num)
        
        return longest