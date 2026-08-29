class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return False
            
            if i == len(nums) -1:
                return True
            
            if nums[i] == 0:
                return False
            
            if i in cache:
                return cache[i]
            
            cache[i] = any([dfs(i+k) for k in range(1, nums[i]+1)])
            return cache[i]
        
        return dfs(0)