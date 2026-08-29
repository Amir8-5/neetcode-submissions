class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opToCl = {'}':'{', ')':"(", ']':'['}
        for c in s:
            if c in opToCl:
                if stack and stack[-1] == opToCl[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        