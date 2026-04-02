# 36 valid sudoku
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for arr in board:
            row = defaultdict(int)
            for i in arr:
                if i != ".":
                    row[i] += 1
                if row[i] > 1:
                    return False
        
        i = j = 0
        while i < 9:
            col = defaultdict(int)
            while j < 9:
                if board[j][i]  != ".":
                    col[board[j][i]] += 1
                if col[board[j][i]] > 1 :
                    return False
                j += 1
            i += 1
            j = 0
                
        i = j = k = l = 0
        while i < 9:
            while j < 9:
                temp = defaultdict(int)
                while k < 3:
                    while l < 3:
                        if board[i + k][j + l]  != ".":
                            temp[board[i + k][j + l]] += 1
                        if temp[board[i + k][j + l]] > 1:
                            return False
                        l += 1
                    k += 1
                    l = 0
                j+=3
                k = l = 0
            i += 3
            j = k = l = 0
        return True