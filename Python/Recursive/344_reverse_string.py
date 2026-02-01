from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(l: int,r: int):
            if r <=  l:
                return 
            s[l], s[r] = s[r], s[l]
            helper(l + 1, r - 1)
        helper(0,len(s)-1)
