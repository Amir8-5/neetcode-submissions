class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) -1
        while s <= e:
            m = (s+e)//2
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                return m

        if nums[m] == target:
            return m
        else:
            return -1
        