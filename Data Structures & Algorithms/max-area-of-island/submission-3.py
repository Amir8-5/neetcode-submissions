class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def maxA(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + maxA(r, c + 1) + maxA(r, c - 1) + maxA(r + 1, c) + maxA(r - 1, c) 
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, maxA(r, c))
        
        return res