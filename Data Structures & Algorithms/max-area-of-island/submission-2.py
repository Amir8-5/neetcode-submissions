class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        cur = 0
        def dfs(i, j):
            nonlocal cur
            nonlocal maxArea
            if i < 0 or j < 0 or i >= ROW or j >= COL or (i, j) in visited or grid[i][j] == 0:
                maxArea = max(maxArea, cur)
                return
            
            visited.add((i, j))
            cur += 1
            print(f"i and j are {(i, j)} and cur is {cur}")
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i , j - 1)
            dfs(i , j + 1)
            
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and (i, j) not in visited:
                    print("calling dfs")
                    dfs(i, j)
                    cur = 0
        return maxArea