from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dc = defaultdict(int)
        for num in nums:
            dc[num] += 1
            if dc [num] > len(nums)//2:
                return num