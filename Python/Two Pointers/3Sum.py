from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        pivot = 0
        ans = set()
        # -2 cuase we can not use the pivot if there are not enougth elements
        while pivot < len(nums) - 2:
            i = pivot + 1
            j = len(nums) - 2
            while i < j:
                s = nums[pivot] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                else:
                    ans.add((nums[pivot], nums[i], nums[j]))
                    i += 1
                    j -= 1
            pivot += 1
        return [list(t) for t in ans]
