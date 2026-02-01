from typing import List, Dict, Set, Tuple, Optional
from collections import deque, defaultdict, Counter

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first get the transpose matrix then the mirror matrix
        n = len(matrix) 
        for a in range(n): 
            for b in range(a, n): 
                matrix[a][b], matrix[b][a] = matrix[b][a], matrix[a][b]

        for a in range(n):
            for b in range(n//2):
                matrix[a][b], matrix[a][n-1-b] = matrix[a][n-1-b],  matrix[a][b]

        