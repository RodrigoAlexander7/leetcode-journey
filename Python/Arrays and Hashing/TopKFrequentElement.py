from typing import List
from collections import Counter

    # firs count the elements
    # then sort the keys by value and store it on an list or something

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        s = len(nums)   # the size of the array
        freq_arr = [[] for _ in range(s + 1)]      # create an array with [[0],[0]...]
        for item in count.items():                  
            freq_arr[item[1]].append(item[0])

        for i in range(s, 0, -1):
            if freq_arr[i] != []:
                for element in freq_arr[i]:
                    ans.append(element)
                    if len(ans) == k: 
                        return ans           # return if rich the k-frequent
        return ans
        



#     # firs count the elements
#     # then sort the keys by value and store it on an list or something

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         dc = defaultdict(int)
        
#         for n in nums:
#             dc[n] += 1
            
#         dc_sorted = dict(sorted(dc.items(), key= lambda i: i[1], reverse=True))        # sorted(each element, key = the value use to sort) -> we use i[i] cause is the second value of the pair on items

#         sorted_list = list(dc_sorted.keys())
#         for i in range(k):  # go all the array form the k element to chek if there are two or more elements with the same count 
#             res.append(sorted_list[i])
#         return res
    
#         # k = 1 | k = 0
        

#         '''
#         mi_dict = {'a': 3, 'b': 1, 'c': 2}
#         mi_dict.items() → [('a', 3), ('b', 1), ('c', 2)]

