class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_filtered = path.replace("/"," ").split()

        for item in path_filtered:
            if item == ".." and len(stack) > 0:
                stack.pop()
            elif item == "." or item == "..":
                continue
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)