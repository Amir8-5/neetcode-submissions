from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            arr.append(-1 * num)
        heapify(arr)

        num = None
        while k > 0:
            print(f"k is {k} and arr is {arr}")
            num = -1 * heappop(arr)
            k -= 1
        return num
