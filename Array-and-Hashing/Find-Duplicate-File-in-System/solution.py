class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentDict = {}

        for path in paths:
            space_split = path.split(' ')
            for i in range(1, len(space_split)):
                curr = space_split[i]
                first = curr.find('(')
                last = curr.find(')')
                content = curr[first + 1: last]

                if content in contentDict:
                    contentDict[content].append(space_split[0] + '/' + curr[:first])
                else:
                    contentDict[content] = [space_split[0] + '/' + curr[:first]]
        
        res = []

        for key, val in contentDict.items():
            if len(val) > 1:
                res.append(val)
        
        return res
