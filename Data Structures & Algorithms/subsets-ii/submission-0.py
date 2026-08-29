class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        sub = []
        def dfs(i):
            if i >= len(nums):
                if sub not in res:
                    res.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res