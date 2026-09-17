class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        sub = []
        def dfs(i):
            s = sum(sub)
            if i == len(nums) or s > target:
                return
            if sum(sub) == target:
                if sub not in res:
                    res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i)
            sub.pop()
            dfs(i+1)
        
        dfs(0)
        return res

        