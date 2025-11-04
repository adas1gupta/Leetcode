class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1

        for i in range(n - 2):
            one, two, three = two, three, one + two + three
        
        return three if n > 0 else 0