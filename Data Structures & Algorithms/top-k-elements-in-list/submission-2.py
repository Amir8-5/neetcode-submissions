class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ordered = [[] for x in range(len(nums)+1)]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            ordered[freq[num]].append(num)
        res = []
        for i in range(len(ordered)-1, 0 , -1):
            for n in ordered[i]:
                res.append(n)
                if len(res) == k:
                    return res