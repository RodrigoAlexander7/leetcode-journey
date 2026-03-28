#242. Valid Anagram
from typing import List
from collections import defaultdict

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
      counter_s = defaultdict(int)
      counter_t = defaultdict(int)

      for letter in s:
         counter_s[letter] += 1
         
      for letter in t:
         counter_t[letter] += 1

      return counter_t == counter_s