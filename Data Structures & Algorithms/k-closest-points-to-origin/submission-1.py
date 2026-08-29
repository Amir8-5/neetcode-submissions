class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for coor in points:
            x2 = coor[0]
            y2 = coor[1]
            distances.append((coor, math.sqrt((0-x2) ** 2 + (0 - y2) ** 2)))
        
        sor = sorted(distances, key=lambda x: x[1])
        print(sor)
        return [x[0] for x in sor[:k]]