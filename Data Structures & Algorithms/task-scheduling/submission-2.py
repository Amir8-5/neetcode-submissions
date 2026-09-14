class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        q = deque()
        while maxHeap or q:
            res += 1
            if not maxHeap:
                res = max(res, q[0][1])
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, res + n])
            
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return res
