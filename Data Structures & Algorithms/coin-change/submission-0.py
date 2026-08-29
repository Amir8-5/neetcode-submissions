class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {i:-1 for i in range(amount+2)}
        print(cache)

        def dfs(target):
            if target == 0:
                return 0
            
            if target < 0:
                return -1
            
            print(f"target was {target}")
            if cache[target] != -1:
                return cache[target]
            
            res = 1e9
            for coin in coins:
                if target - coin >= 0:
                    res = min(res, 1 + dfs(target - coin))
            cache[target] = res
            return res
        minAmount = dfs(amount)
        return -1 if minAmount >= 1e9 else minAmount