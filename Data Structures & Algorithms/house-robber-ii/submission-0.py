class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        withLast = nums[1:]
        withoutLast = nums[:-1]
        cache = [[-1] * 2 for _ in range(n)]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == n - 1):
                return 0
            
            if cache[i][flag] != -1:
                return cache[i][flag]
            
            cache[i][flag] = max(nums[i] + dfs(i+2, flag or (i == 0)), dfs(i+1, flag))
            return cache[i][flag]

        return max(nums[0], dfs(0, True), dfs(1, False))

