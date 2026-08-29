class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)
        for i in range(len(nums)):
            prod = None
            for j in range(len(nums)):
                if prod == None and j != i:
                    prod = nums[j]
                elif j != i:
                    prod *= nums[j]
            output[i] = prod
        return output
        