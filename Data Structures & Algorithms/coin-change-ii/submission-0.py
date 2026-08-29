class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = defaultdict(lambda: -1, {})

        def dfs(i, current):
            if current == amount:
                return 1
            
            if current > amount:
                return 0
            
            if i >= len(coins):
                return 0
            
            if cache[(i, current)] != -1:
                return cache[(i, current)]
            
            cache[(i, current)] = dfs(i, current+coins[i]) + dfs(i+1, current)
            return cache[(i, current)]
        
        return dfs(0, 0)
            
