class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        m, n = len(word1), len(word2)

        def dfs(i, j):
            if i == m:
                return n-j
            
            if j == n:
                return m - i
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if word1[i] != word2[j]:
                res = min(dfs(i+1, j), dfs(i, j+1))
                res = min(res, dfs(i+1, j+1))
                cache[(i, j)] = 1 + res
            else:
                cache[(i, j)] = dfs(i+1, j+1)
            
            return cache[(i, j)]
        return dfs(0, 0)