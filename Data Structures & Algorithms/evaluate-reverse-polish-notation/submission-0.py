class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                snd = stack.pop()
                fst = stack.pop()
                stack.append(fst - snd)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                snd = stack.pop()
                fst = stack.pop()
                stack.append(int(fst / snd))
            else:
                stack.append(int(c))
        return stack[0]
