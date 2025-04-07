class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()

        def helper(path, used):
            if len(path) == 3:
                if path[0] != 0 and path[2] % 2 == 0:
                    number = path[0] * 100 + path[1] * 10 + path[2]
                    result.add(number)
                
            
            for i in range(len(used)):
                if used[i]:
                    continue
                used[i] = True
                path.append(digits[i])
                helper(path, used)
                path.pop()
                used[i] = False 
        
        helper([], [False] * len(digits))
        return len(result)