# 242. Valid Anagram
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        start = intervals[0][0]     # [start ,end] shapes the current interval
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            # the range -> [a,b]
            a = intervals[i][0]
            b = intervals[i][1]
            if (a <= end):
                end = max(b, end)
            else:
                res.append([start, end])
                start = a
                end = b

        # adding the last interval
        res.append([start, max(end,intervals[len(intervals)-1][1])])
        

        return res
