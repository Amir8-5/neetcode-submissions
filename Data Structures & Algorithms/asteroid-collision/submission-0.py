class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            while stack and num < 0 and stack[-1] > 0:
                diff = stack[-1] + num
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    num = 0
                else:
                    num = 0
                    stack.pop()
            
            if num:
                stack.append(num)

        return stack