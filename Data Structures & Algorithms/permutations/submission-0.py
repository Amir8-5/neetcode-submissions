class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        sub = []
        def dfs(arr):
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            
            for i in range(len(arr)):
                num = arr[i]
                if num not in sub:
                    sub.append(num)
                    dfs(arr)
                    sub.pop()
        dfs(nums)
        return res
        