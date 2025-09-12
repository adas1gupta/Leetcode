import math
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        operator = '+'
        s = s.replace(" ", "").strip()

        def operation(operator: str):
            match operator:
                case '+':
                    stack.append(curr)
                case '-':
                    stack.append(-curr)
                case '*':
                    stack.append(curr * stack.pop())
                case '/':
                    stack.append(math.trunc(stack.pop() / curr))

        for item in s:
            if item in '+-*/':
                operation(operator)
                operator = item
                curr = 0
            else:
                curr = curr * 10 + int(item)
        
        operation(operator)
        
        return sum(stack)