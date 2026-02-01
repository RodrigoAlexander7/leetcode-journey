from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        start = 0
        end = 1
        res = []
        while i < len(nums):
            if end < len(nums) and nums[i] + 1 == nums[end]:
                end += 1
            elif start != end - 1:
                res.append(f"{nums[start]}->{nums[end - 1]}")
                start = end
                end += 1
            else:
                res.append(str(nums[end - 1]))
                start = end
                end += 1
            i += 1
        return res
