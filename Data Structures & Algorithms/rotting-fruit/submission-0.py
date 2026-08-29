class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fresh = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        def addRotten(r, c):
            nonlocal fresh
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0 or grid[r][c] == 2 or (r, c) in visited:
                return
            
            visited.add((r, c))
            q.append([r, c])
            fresh -= 1
        
        def isAllRotten():
            for i in range(ROW):
                for j in range(COL):
                    if grid[i][j] == 1:
                        return False
            return True
        
        mint = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                addRotten(r - 1, c)
                addRotten(r + 1, c)
                addRotten(r, c - 1)
                addRotten(r, c + 1)
            mint += 1
        return mint if fresh == 0 else -1