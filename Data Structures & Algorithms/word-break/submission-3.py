class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [-1] * len(s)
        def dfs(st, i):
            if len(st) == 0:
                return True
            if cache[i] != -1:
                return cache[i]
            words = self.starts(st, wordDict)
            for word in words:
                if dfs(st[len(word):], i+len(word)):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return False

        return dfs(s, 0)

    def starts(self, s, words):
        res = []
        for word in words:
            if s.startswith(word):
                res.append(word)
        return res