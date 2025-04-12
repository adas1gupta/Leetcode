class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            prev = result[-1]
            
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                result.append(interval)
        
        return result