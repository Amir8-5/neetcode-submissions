class PreNode:

    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = PreNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = PreNode()
            cur = cur.children[c]
        print(f"inserted: {word}")
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                print(f"search false: {word}")
                return False
        print(f"search true: {word} and end: {cur.end}")
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                print(f"startsWith false: {prefix}")
                return False
        print(f"startsWith true: {prefix}")
        return True
        
        