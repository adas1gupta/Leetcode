class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maximum = 1
        scanner = 1
        curr = 1

        while scanner < len(s):
            if ord(s[scanner]) - 1 == ord(s[scanner - 1]):
                curr += 1
            else:
                curr = 1
            
            maximum = max(curr, maximum)
            scanner += 1

        return maximum 