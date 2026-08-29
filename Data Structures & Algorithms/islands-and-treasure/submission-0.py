class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        FILL = 2147483647
        visited = set()
        q = deque()
        ROW, COL = len(grid), len(grid[0])

        def addRoom(r, c):
            if r >= ROW or r < 0 or c >= COL or c < 0 or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append([r, c])
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
                addRoom(r, c + 1)
            dist += 1
        
        