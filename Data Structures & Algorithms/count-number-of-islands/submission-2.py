class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rLen, cLen = len(grid), len(grid[0])

        def rect (r, c):
            if r < 0 or r >= rLen or c < 0 or c >= cLen or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            rect(r + 1, c)
            rect(r - 1, c)
            rect(r, c + 1)
            rect(r, c - 1)
        
        res = 0
        for r in range(rLen):
            for c in range(cLen):
                if grid[r][c] == "1":
                    rect(r, c)
                    res += 1
        return res

            

            

            