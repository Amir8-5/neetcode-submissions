class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digToLet = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        sub = []
        def dfs(word):
            if len(sub) >= len(digits):
                res.append("".join(sub))
                return
            
            first = word[0]
            lets = digToLet[first]
            for char in lets:
                sub.append(char)
                print(f"word is {word}")
                dfs(word[1:])
                sub.pop()
        dfs(digits)
        return res
