class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        newPoints = [[-1 * math.sqrt((x[0]**2) + (x[1]**2)), x] for x in points]
        heapq.heapify(newPoints)

        while len(newPoints) > k:
            heapq.heappop(newPoints)
        
        return [x[1] for x in newPoints]