class Solution:
    def nextGreaterElement(self, n: int) -> int:
        string = str(n)
        start, end = len(string) - 2, len(string) - 1
        pivot = None

        while start >= 0:
            if int(string[end]) > int(string[start]):
                pivot = start
                break
            end -= 1
            start -= 1

        if pivot == None:
            return -1

        ptr = len(string) - 1
        next_smallest = None
        while ptr > pivot:
            if int(string[ptr]) > int(string[pivot]):
                next_smallest = ptr
                break
            ptr -= 1 

        if next_smallest is not None:
            string_list = list(string)
            string_list[pivot], string_list[next_smallest] = string_list[next_smallest], string_list[pivot]
            string_list[pivot + 1:] = string_list[pivot + 1:][::-1]
            res = int("".join(string_list))

            if res > 2 ** 31 - 1:
                return -1
            else:
                return res
        else:
            return -1