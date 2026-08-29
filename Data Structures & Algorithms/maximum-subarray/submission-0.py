class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = [[None] * 2 for _ in range(len(nums)+1)]

        def dfs(i, flag):
            if i >= len(nums):
                return 0 if flag else -1e6
            
            if cache[i][flag] is not None:
                return cache[i][flag]
            
            if flag:
                cache[i][flag] = max(0, nums[i] + dfs(i+1, True))
            else:
                cache[i][flag] = max(dfs(i+1, False), nums[i]+ dfs(i+1, True))
            return cache[i][flag]
        
        return dfs(0, False)