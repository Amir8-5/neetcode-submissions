class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
         
        while len(stones) > 1:
            stones.sort()
            x, y = stones.pop(len(stones)-1), stones.pop(len(stones) - 1)
            if x == y:
                pass
            elif x > y:
                stones.append(x - y)
            
            print(f"{stones} after {x}, {y}")
        if stones:
            return stones[0]
        else:
            return 0    
        