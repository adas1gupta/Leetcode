class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            if sChar not in sDict:
                sDict[sChar] = [1, tChar]
            else:
                sDict[sChar][0] += 1
            
            if tChar not in tDict:
                tDict[tChar] = [1, sChar]
            else:
                tDict[tChar][0] += 1
            
            if tDict[tChar][0] != sDict[sChar][0] or sDict[sChar][1] != tChar:
                return False

        return True