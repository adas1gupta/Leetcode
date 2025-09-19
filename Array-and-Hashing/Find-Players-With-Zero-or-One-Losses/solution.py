class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        never_lost = set()
        lost_once = {}

        for item in matches:
            _, val = item[0], item[1]
            lost_once[val] = lost_once.get(val, 0) + 1
        
        for item in matches:
            winner, _ = item[0], item[1]
            if winner not in lost_once:
                never_lost.add(winner)
        
        one_loss = []

        for key, val in lost_once.items():
            if val == 1:
                one_loss.append(key)
        
        ans.append(sorted(list(never_lost)))
        ans.append(sorted(one_loss))
    
        return ans