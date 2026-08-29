class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for o in operations:
            if o == "+" and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])
            elif o == "D" and stack:
                stack.append(stack[-1] * 2)
            elif o == "C" and stack:
                stack.pop()
            else:
                stack.append(int(o))
        
        return sum(stack)

