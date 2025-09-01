class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left, right = 0, 0
        l = 0
        r = 0
        while left < len(start) or right < len(target):
            while left < len(start) and start[left] == "_":
                left += 1
            
            while right < len(target) and target[right] == "_":
                right += 1
            
            if left == len(start) or right == len(target):
                return left == len(start) and right == len(target)
                

            if start[left] == "L" and left < right:
                return False
            elif start[left] == "R" and left > right:
                return False
            elif start[left] != target[right]:
                return False

            left += 1
            right += 1
        
        return True