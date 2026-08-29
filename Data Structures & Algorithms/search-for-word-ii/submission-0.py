class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        cur.word = word
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Trie()
        for word in words:
            tree.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if ((r < 0 or c < 0) or (r >= len(board) or c >= len(board[0])) 
                or ((r, c) in visit) or (board[r][c] not in node.children)):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, tree.root, "")
        return list(res)


        
