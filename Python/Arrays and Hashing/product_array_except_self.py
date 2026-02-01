# 238. Product of Array Except Self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = []
        # Calculate all the prefix
        prefix_aux = 1
        for i in range(len(nums)):
            prefix.append(prefix_aux)
            prefix_aux *= nums[i]

        sufix = (
            [0] * len(nums)
        )  # initialize an array with 0 -> important cause we need to fill the array since the last element
        # Calculate all the sufix
        sufix_aux = 1
        for i in range(
            len(nums) - 1, -1, -1
        ):  # the las two -1 means -> repeat until the -1th element and decrece in 1 each step
            sufix[i] = sufix_aux
            sufix_aux *= nums[i]

        for i in range(len(nums)):
            res.append(prefix[i] * sufix[i])

        return res
