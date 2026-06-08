from collections import defaultdict
from typing import List


# Bruteforce solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            start, end = i, len(height) - 1
            while start < end:
                width = end - start
                max_water = max(max_water, min(height[start], height[end]) * width)
                end -= 1
        return max_water


# Optimal solution


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        start, end = 0, len(height) - 1
        while start < end:
            width = end - start
            max_water = max(max_water, min(height[start], height[end]) * width)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_water
