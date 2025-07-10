class Solution:

    def encode(self, strs: List[str]) -> str:
        length = [0] * len(strs)

        for ind, item in enumerate(strs):
            length[ind] = len(item)

        res = ""

        for ind in range(len(strs)):
            to_add = f"{length[ind]}%{strs[ind]}"
            res += to_add

        return res

    def decode(self, s: str) -> List[str]:
        to_return = []

        ind = 0
        n = len(s)

        while ind < n:
            j = ind
            while s[j] != '%':
                j += 1

            num = int(s[ind:j])
            to_return.append(s[j + 1: j + 1 + num])
            ind = j + 1 + num

        return to_return 