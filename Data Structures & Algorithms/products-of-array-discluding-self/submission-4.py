class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        zero = 0

        prod = 1
        for num in nums:
            if num:
                prod *= num
            else:
                zero += 1
        
        if zero > 1:
            return [0] * n
        

        for i, c in enumerate(nums):
            if zero: 
                res[i] = 0 if c else prod
            else: 
                res[i] = prod // c
        return res

        