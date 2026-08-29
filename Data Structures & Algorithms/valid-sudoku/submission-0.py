class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == '.':
                    continue
                
                if item in row[r] or item in col[c] or item in box[(r // 3, c // 3)]:
                    return False
                
                row[r].add(item)
                col[c].add(item)
                box[(r // 3, c // 3)].add(item)
        
        return True
        