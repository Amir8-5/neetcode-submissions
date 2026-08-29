class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq.items():
            bucket[cnt].append(num)
        

        res = []
        chosen = 0
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                chosen += 1
                if chosen == k:
                    return res
