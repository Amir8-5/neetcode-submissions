class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        cache = defaultdict(lambda:-1001, cache)

        def dfs(i, prev):
            if i >= n:
                return 0
            
            if cache[(i, prev)] != -1001:
                return cache[(i, prev)]
            
            if nums[i] > prev:
                cache[(i, nums[i])] = max(1+dfs(i+1, nums[i]), dfs(i+1, prev))
            else:
                cache[(i, prev)] = dfs(i+1, prev)
            
            return max(cache[(i, nums[i])], cache[(i, prev)])
        
        return dfs(0, -1001)