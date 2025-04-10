class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(opn, close, path):
            if len(path) == 2 * n:
                res.append(path)
                return
            
            if opn < n:
                helper(opn + 1, close, path + "(")
            if close < opn:
                helper(opn, close + 1, path + ")")

        helper(0, 0, "")
        return res