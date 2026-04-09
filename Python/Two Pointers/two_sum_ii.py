from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        ans = []

        while i < j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i + 1,j + 1]
            if current > target:
                j -= 1
            else:
                i += 1
