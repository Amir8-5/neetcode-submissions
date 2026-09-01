class Solution:
    def reverseBits(self, n: int) -> int:
        temp = 0
        for i in range(32):
            if ((n >> i) & 1) == 1:
                temp |= (1 << (31-i))
        
        return temp