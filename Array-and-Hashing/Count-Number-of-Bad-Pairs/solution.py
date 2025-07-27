class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        numPairs = (n * (n - 1) // 2)
        numDict = {}
        
        for i, num in enumerate(nums):
            diff = i - num
            numDict[diff] = numDict.get(diff, 0) + 1
            
        for key, val in numDict.items():
            numPairs -= (val * (val - 1) // 2)
        
        return numPairs
        