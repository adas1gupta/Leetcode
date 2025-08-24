class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = version1.split(".")
        second = version2.split(".")

        shorter = min(len(first), len(second))
        crsr = 0

        while crsr < shorter:
            f_n = int(first[crsr])
            s_n = int(second[crsr])

            if f_n < s_n:
                return -1
            elif f_n > s_n:
                return 1
            
            crsr += 1
        
        while crsr < len(first):
            if int(first[crsr]) != 0:
                return 1
            crsr += 1

        while crsr < len(second):
            if int(second[crsr]) != 0:
                return -1
            crsr += 1
        
        return 0