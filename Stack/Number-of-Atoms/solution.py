class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        ind, n = 0, len(formula)

        while ind < n:
            item = formula[ind]

            if item == "(":
                stack.append({})
                ind += 1
            
            elif item == ")":
                ind += 1
                start = ind

                while start < n and formula[start].isdigit():
                    start += 1

                num = int(formula[ind: start] or 1)
                ind = start

                for key, val in stack[-1].items():
                    stack[-1][key] *= num
                
                nested_level = stack.pop()
                
                for key, val in nested_level.items():
                    stack[-1][key] = stack[-1].get(key, 0) + val
                

            else:
                start = ind + 1

                while start < n and formula[start].islower():
                    start += 1
                
                elem = formula[ind: start]

                ind = start
                start = ind

                while start < n and formula[start].isdigit():
                    start += 1
                
                num = int(formula[ind: start] or 1)
                
                ind = start

                stack[-1][elem] = stack[-1].get(elem, 0) + num

        res = []
        for key in sorted(stack[-1].keys()):
            res.append(key)

            if stack[-1][key] != 1:
                res.append(str(stack[-1][key]))
        
        return ''.join(res)