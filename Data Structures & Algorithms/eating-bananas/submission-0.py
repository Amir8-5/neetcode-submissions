import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        smallest = r
        while l <= r:
            mid = (l + r) // 2
            hours = self.getHours(mid, piles)
            if hours > h:
                l = mid + 1
            else:
                if mid < smallest:
                    smallest = mid
                    r = mid - 1
                else:
                    r = mid - 1
        return smallest

    def getHours(self, k, piles):
        h = 0
        for pile in piles:
            h += math.ceil(pile/k)
        return h

        