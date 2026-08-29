class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[-1] * 2 for _ in range(n)]

        def dfs(i, owned):
            if i >= n:
                return 0
            
            if cache[i][owned] != -1:
                return cache[i][owned]
            
            noChange = dfs(i+1, owned)
            if owned:
                cache[i][owned] = max(prices[i]+dfs(i+2, 0), noChange)
            else:
                cache[i][owned] = max(dfs(i+1,1) - prices[i], noChange)
            return cache[i][owned]

        return dfs(0, 0) 