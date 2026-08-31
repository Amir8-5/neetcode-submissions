class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])


        q = deque()
        level = 0
        self.fresh = 0

        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                
                if grid[r][c] == 1:
                    self.fresh += 1
        
        def addCell(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r,c))
            self.fresh -= 1

        while q and self.fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r, c + 1)
                addCell(r, c - 1)
                addCell(r + 1, c)
                addCell(r - 1, c)
            level += 1
        
        
        
        
        return level if self.fresh == 0 else -1
