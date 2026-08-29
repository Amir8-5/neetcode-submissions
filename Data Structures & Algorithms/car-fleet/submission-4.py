class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPlaces = [(p, s) for p, s in zip(position, speed)]
        carPlaces.sort(reverse=True)
        
        stack = []
        for p, s in carPlaces:
            finish = (target - p) / s
            if not stack:
                stack.append(float(finish))
            elif finish > stack[-1]:
                stack.append(float(finish))
        return len(stack)