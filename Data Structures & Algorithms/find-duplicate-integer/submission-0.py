class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                return num
                
        