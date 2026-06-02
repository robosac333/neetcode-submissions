class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        allowed = "[{("
        pairs = {"[":"]", "{":"}", "(":")"}
        if len(s)==1:
            return False
        for candidate in s:
            if candidate in allowed:
                stack.append(candidate)
            else:
                if not stack:
                    return False
                compare = stack.pop()
                if pairs[compare]!=candidate:
                    return False
        if stack:
            return False
        return True
