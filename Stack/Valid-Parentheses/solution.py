class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for item in s:
            if item not in brackets:
                stack.append(item)
            elif len(stack) == 0:
                return False
            else:
                pair = stack.pop()
                if brackets[item] != pair:
                    return False
        
        return True if len(stack) == 0 else False