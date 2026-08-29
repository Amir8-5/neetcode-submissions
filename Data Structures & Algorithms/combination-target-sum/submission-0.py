class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sub = []
        def dfs(i, sums):
            if i >= len(nums) or sums > target:
                return
            
            if sums == target:
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(i, sums + nums[i])

            sub.pop()
            dfs(i+1, sums)
        
        dfs(0, 0)
        return res
