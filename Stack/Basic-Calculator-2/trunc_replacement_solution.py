class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        last_op = '+'
        curr = 0

        def operation_handling(op: str):
            match op:
                case '-':
                    stack.append(-curr)
    
                case '+':
                    stack.append(curr)
                    
                case '*':
                    stack.append(stack.pop() * curr)

                case "/":
                    dividend = stack.pop()
                    to_append = abs(dividend) // abs(curr)
                    to_append = to_append if dividend * curr > 0 else -to_append
                    stack.append(to_append)

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            
            else:
                operation_handling(last_op)
                curr = 0
                last_op = char

        operation_handling(last_op)

        return sum(stack)
