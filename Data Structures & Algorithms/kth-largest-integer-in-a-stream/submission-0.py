class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.vals = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        self.vals.append(val)
        self.vals = sorted(self.vals)
        return self.vals[len(self.vals) - self.k]
            
            

 