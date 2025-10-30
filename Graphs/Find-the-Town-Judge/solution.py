class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
            
        citizens = {}
        judge = {}

        for item in trust:
            cit, cand = item[0], item[1]

            citizens[cit] = citizens.get(cit, 0) + 1
            judge[cand] = judge.get(cand, 0) + 1
        
        for item in judge.keys():
            if judge[item] == n - 1 and item not in citizens:
                return item
        
        return -1