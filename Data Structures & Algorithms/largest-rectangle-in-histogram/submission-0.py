class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0
        
        for i, h in enumerate(heights):
            ind = i
            while stack and h <= stack[-1][1]:
                ind, num = stack.pop()
                maxA = max(maxA, num * (i - ind))
            
            stack.append((ind, h))
        
        for i, h in stack:
            maxA = max(maxA, (len(heights) - i) * h)
        
        return maxA
        
