class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                left = mid + 1
            else:
                start, end = 0, len(matrix[0]) - 1

                while start <= end:
                    m = start + (end - start) // 2
                    
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        start = m + 1
                    else:
                        end = m - 1
                
                return False
        
        return False