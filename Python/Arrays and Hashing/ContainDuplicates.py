from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        aux = set()
        for num in nums:
            if num in aux:
                return True
            aux.add(num)
        return False
