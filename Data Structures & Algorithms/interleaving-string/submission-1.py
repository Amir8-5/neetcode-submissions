class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, f = len(s1), len(s2), len(s3)
        if m+n != f:
            return False
        
        cache = {}
        def dfs(i, j):
            if i == m and j == n:
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            k = i + j
            if  i < m and s1[i] == s3[k] and dfs(i+1, j):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j+1):
                return True
            
            cache[(i, j)] = False
            return False
            
        
        return dfs(0, 0)
            

            
