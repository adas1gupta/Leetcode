class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        
        def helper(opn, close, path):
            if len(path) == (2 * n):
                if opn == close:
                    res.add(path)
                return 

            if close < opn:
                close_path = path + ")"
                new_path = path + "("
                helper(opn, close + 1, close_path)
                helper(opn + 1, close, new_path)
            else:
                new_path = path + "("
                helper(opn + 1, close, new_path)
        
        helper(0, 0, "")
        return list(res)