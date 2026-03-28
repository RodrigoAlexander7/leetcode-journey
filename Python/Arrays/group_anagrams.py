from typing import List
from collections import defaultdict

'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

key -> counter of chars
value -> the lists of words

dc = {}
for s on strings:
    aux = [0] * 26 // array that representa the alpabeth to counter letters
    # count the letters on a tuple
    if (tuple is on dc.keys) // means that an anagram already exist (justa append it) 
        dc[tuple].append(s)
    else
        # add the dict    


    
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())        