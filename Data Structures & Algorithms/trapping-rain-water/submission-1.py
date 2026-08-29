class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0
        maxL, maxR = [0] * len(height), [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                maxL[i] = height[i]
            else:
                maxL[i] = max(height[i], maxL[i-1])


        maxN = 0
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                maxR[i] = height[i]
            else:
                maxR[i] = max(height[i], maxR[i+1])


        res = 0
        for i in range(len(height)):
            res += min(maxL[i], maxR[i]) - height[i]
        
        return res
        

