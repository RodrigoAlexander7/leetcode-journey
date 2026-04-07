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
            if i - 1 in st:
                continue
            else:
                while i + 1 in st:
                    ans += 1
                    st.remove(i)
                    i += 1
