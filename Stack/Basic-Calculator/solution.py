class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0 #used to record the number that you're on
        total = 0 #used to measure the value accumulated so far
        s = s.replace(" ", "")
        prev_op = "+"

        for item in s:
            if item.isdigit():
                curr = curr * 10 + int(item)
            
            elif item == "+":
                match prev_op:
                    case "+":
                        total += curr
                    case '-':
                        total -= curr 
                
                prev_op = item
                curr = 0

            elif item == "-":
                match prev_op:
                    case "+":
                        total += curr
                    case '-':
                        total -= curr 
                
                prev_op = item
                curr = 0

            elif item == "(":
                stack.append(total)
                stack.append(prev_op)

                prev_op = '+'
                total = 0
            
            elif item == ")":
                match prev_op:
                    case "+":
                        total += curr
                    case '-':
                        total -= curr
                        
                prev_sign = stack.pop()
                prev_total = stack.pop()

                match prev_sign:
                    case "+":
                        total = total + prev_total
                    case '-':
                        total = prev_total - total
                
                curr = 0
        
        match prev_op:
            case "+":
                total += curr
            case '-':
                total -= curr
        
        return total