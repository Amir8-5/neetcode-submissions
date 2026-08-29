class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key= lambda tup:tup[0])
        copy = intervals.copy()
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                res.append(intervals[i-1])
            else:
                intervals[i] = [min(intervals[i][0], intervals[i-1][0]), max(intervals[i][1], intervals[i-1][1])]
        res.append(intervals[-1])
        return res
