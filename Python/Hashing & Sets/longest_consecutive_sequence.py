# 128 Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()

        if not nums:
            return 0

        for num in nums:
            st.add(num)


        ans = 1
        for i in st:
            if not i - 1 in st:
                length = 1
                while i + 1 in st:
                    length += 1
                    i += 1
                ans = ans if ans > length else length
        return ans
