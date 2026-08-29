class MinStack:
    _lst : List

    def __init__(self):
        self._lst = []
        
    def push(self, val: int) -> None:
        self._lst.append(val)

    def pop(self) -> None:
        self._lst.pop()

    def top(self) -> int:
        top = self._lst.pop()
        self._lst.append(top)
        return top

    def getMin(self) -> int:
        return min(self._lst)
        
