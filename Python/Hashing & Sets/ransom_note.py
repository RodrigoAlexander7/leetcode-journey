# 383. Ransom Note
from typing import List
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = defaultdict(int)
        for letter in magazine:
            dct[letter] += 1
        
        for i in ransomNote:
            dct[i] -= 1
            if dct[i] < 0:
                return False 
        return True 