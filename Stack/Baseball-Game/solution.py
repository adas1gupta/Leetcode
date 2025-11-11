class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            
            elif op == "D":
                stack.append(stack[-1] * 2)
            
            elif op == "+":
                first, second = stack.pop(), stack.pop()
                top_two = first + second
                
                stack.append(second)
                stack.append(first)
                stack.append(top_two)

            else:
                stack.append(int(op))
                  
        return sum(stack)