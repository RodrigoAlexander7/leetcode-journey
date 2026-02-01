# 54. Spiral Matrix

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = left = 0
        right = len(matrix[0])
        down =  len(matrix) 


        while(down > top  and right > left):
            for c in range(left,right):
                res.append(matrix[top][c])
            top += 1

            for r in range(top, down):
                res.append(matrix[r][right - 1])    # right is unbounded
            right -=1

            if not (down > top and right > left):
                break

            for c in range(right-1, left - 1, -1): # right - 1 -> right is unbounded by initialization  |  left - 1 -> to include the las index 
                res.append(matrix[down - 1][c])     # down is unbounded
            down -= 1

            for r in range(down - 1, top - 1, -1):
                res.append(matrix[r][left])
            left+=1

        return res
