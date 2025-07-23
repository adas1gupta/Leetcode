class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        left, right = 0, 1
        order_dict = {}

        for ind, char in enumerate(order):
            order_dict[char] = ind

        while left < right < len(words):
            first = words[left]
            second = words[right]

            ptr = 0
            while ptr < len(first) and ptr < len(second):
                first_char = first[ptr]
                second_char = second[ptr]

                if order_dict[first_char] > order_dict[second_char]:
                    return False
                elif order_dict[first_char] == order_dict[second_char]:
                    ptr += 1
                else:
                    break
            
            if len(first) > len(second) and ptr == len(second):
                return False
            
            left += 1
            right += 1

        return True