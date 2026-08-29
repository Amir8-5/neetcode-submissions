class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        sub = []
        def dfs(i, sums):
            if sums == target:
                res.append(sub.copy())
                return

            if i == len(candidates) or sums > target:
                return
            
            sub.append(candidates[i])
            dfs(i + 1, sums + candidates[i])

            sub.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sums)
            
            
        
        dfs(0, 0)
        return res