import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for item in tokens:
            match item:
                case '+':
                    first = nums.pop()
                    second = nums.pop()
                    nums.append(first + second)
                case '-':
                    first = nums.pop()
                    second = nums.pop()
                    nums.append(second - first)
                case '*':
                    first = nums.pop()
                    second = nums.pop()
                    nums.append(first * second)
                case '/':
                    first = nums.pop()
                    second = nums.pop()
                    nums.append(math.trunc(second / first))
                case _:
                    nums.append(int(item))

        return nums[-1]