class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def findIf(visited, i, j, wor):
            if len(wor) == 0:
                return True
            
            if (i < len(board) and i >= 0) and (j < len(board[i]) and j >= 0):
                if board[i][j] == wor[0] and not visited[i][j]:
                    visited[i][j] = True
                    x = []
                    x.append(findIf(visited, i + 1, j, wor[1:]))
                    x.append(findIf(visited, i - 1, j, wor[1:]))
                    x.append(findIf(visited, i, j + 1, wor[1:]))
                    x.append(findIf(visited, i , j - 1, wor[1:]))
                    visited[i][j] = False
                    return any(x)
                else:
                    return False
            else:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                lett = board[i][j]
                if lett == word[0] and findIf(visited, i, j, word):
                    return True
        return False
