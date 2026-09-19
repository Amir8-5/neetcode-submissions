class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(i, cur):
            if i == len(nums):
                if cur not in res:
                    res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            while i < len(nums) - 1 and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1, cur)
        
        dfs(0, [])
        return res