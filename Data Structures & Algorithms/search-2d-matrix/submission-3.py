class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] == target:
                return True
            elif matrix[m][0] < target and matrix[m][len(matrix[m]) - 1] < target:
                l = m + 1
            else:
                return self.searchNums(matrix[m], target)
        return False
    
    def searchNums(self, nums, target) -> bool:
        l , r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else :
                return True
        return False
        