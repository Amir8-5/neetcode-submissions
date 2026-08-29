class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(opN, clN):
            if opN == clN == n:
                res.append(''.join(stack))
                return
            
            if opN < n:
                stack.append('(')
                backtrack(opN + 1, clN)
                stack.pop()
            
            if clN < opN:
                stack.append(')')
                backtrack(opN, clN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

        