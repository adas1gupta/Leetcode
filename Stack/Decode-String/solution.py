class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_list = []
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            elif char == "[":
                stack.append((current_num, current_list))
                current_list = []
                current_num = 0
            
            elif char == ']':
                repeat_count, prev_list = stack.pop()
                current_list = prev_list + (current_list * repeat_count)
            
            else:
                current_list.append(char)
        
        return ''.join(current_list)