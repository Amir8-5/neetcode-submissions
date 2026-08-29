class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                elif nums[mid] < target and target > nums[r]:
                    r = mid - 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid]:
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    l = mid + 1
        return -1


    def binary(self, nums: List[int], target: int) -> int:
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
        