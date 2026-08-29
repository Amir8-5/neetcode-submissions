class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i , j - 1)
            dfs(i , j + 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands
